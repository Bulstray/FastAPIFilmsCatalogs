from typing import Any

import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from starlette.testclient import TestClient

from main import app
from tests.conftest import build_movie_random_slug


class TestCreateInvalid:

    @pytest.fixture(
        params=[
            pytest.param(("a", "string_too_short"), id="too_short"),
            pytest.param(("foo-bar-spam-eggs", "string_too_long"), id="too_long"),
        ],
    )
    def movie_create_value(
        self,
        request: SubRequest,
    ) -> tuple[dict[str, Any], str]:
        name, description = request.param
        build = build_movie_random_slug(description=description, name=name)
        data = build.model_dump(mode="json")
        slug, err_type = request.param
        data["slug"] = slug
        return data, err_type

    def test_invalid_slug(
        self,
        movie_create_value: tuple[dict[str, Any], str],
        auth_client: TestClient,
    ) -> None:
        url = app.url_path_for("add_film")
        create_data, expected_error_type = movie_create_value
        response = auth_client.post(url=url, json=create_data)
        assert (
            response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        ), response.text

        error_detail = response.json()["detail"][0]
        assert error_detail["type"] == expected_error_type, error_detail
