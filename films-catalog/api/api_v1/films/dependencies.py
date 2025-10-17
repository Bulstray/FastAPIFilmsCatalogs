import logging

from fastapi import (
    HTTPException,
    status,
)
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)

from services.auth import redis_tokens

log = logging.getLogger(__name__)

static_api_token = HTTPBearer(
    auto_error=False,
    scheme_name="Static API token",
    description="Your Static API token from the developer portal",
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
