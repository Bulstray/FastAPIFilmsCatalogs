import logging
from typing import Annotated

from fastapi import (
    Depends,
    HTTPException,
    Request,
    status,
)
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
)

from schemas.movie import Movie

from ..auth.services.redis_tokens_helper import redis_tokens
from ..auth.services.redis_users_helper import redis_users
from .crud import storage

log = logging.getLogger(__name__)

UNSAFE_METHODS = frozenset(
    {
        "PUT",
        "PATCH",
        "DELETE",
        "POST",
    },
)

static_api_token = HTTPBearer(
    auto_error=False,
    scheme_name="Static API token",
    description="Your Static API token from the developer portal",
)


def prefetch_film_by_id(slug: str) -> Movie:
    film: Movie | None = storage.get_by_slug(slug=slug)
    if film:
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {slug!r} not found",
    )


user_basic_auth = HTTPBasic(
    scheme_name="Basic Auth",
    description="Basic username + password auth",
    auto_error=False,
)


def validate_api_token(api_token: HTTPAuthorizationCredentials) -> None:
    if redis_tokens.token_exist(
        token=api_token.credentials,
    ):
        return
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API token",
    )


def validate_basic_auth(credentials: HTTPBasicCredentials | None) -> None:

    if credentials and redis_users.validate_user_password(
        username=credentials.username,
        password=credentials.password,
    ):
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


def api_token_or_auth_required_for_unsafe_methods(
    request: Request,
    api_token: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(static_api_token),
    ] = None,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(user_basic_auth),
    ] = None,
) -> None:
    if request.method not in UNSAFE_METHODS:
        return

    if credentials:
        return validate_basic_auth(
            credentials=credentials,
        )

    if api_token:
        return validate_api_token(
            api_token=api_token,
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="API token or basic auth required",
    )
