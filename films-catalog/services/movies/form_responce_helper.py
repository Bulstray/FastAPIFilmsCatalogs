from typing import Any, Mapping

from pydantic import BaseModel, ValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse

from templating import templates


class FormResponseHelper:
    def __init__(
        self,
        model: type[BaseModel],
        template_name: str,
    ) -> None:
        self.model = model
        self.template_name = template_name

    @staticmethod
    def format_pydantic_errors(
        error: ValidationError,
    ) -> dict[str, str]:
        return {f"{err["loc"][0]}": err["msg"] for err in error.errors()}

    def render(
        self,
        request: Request,
        form_data: BaseModel | Mapping[str, Any] | None = None,
        *,
        form_validated: bool = False,
        pydantic_errors: ValidationError | None = None,
        errors: dict[str, str] | None = None,
        **context_extra: object,
    ) -> HTMLResponse:

        if pydantic_errors:
            errors = self.format_pydantic_errors(pydantic_errors)

        context: dict[str, Any] = {}
        model_schema = self.model.model_json_schema()
        context.update(
            model_schema=model_schema,
            errors=errors,
            form_validated=form_validated,
            form_data=form_data,
        )

        context.update(context_extra)

        return templates.TemplateResponse(
            request=request,
            name=self.template_name,
            context=context,
            status_code=(
                (
                    status.HTTP_422_UNPROCESSABLE_ENTITY
                    if form_validated and errors
                    else status.HTTP_200_OK
                )
            ),
        )
