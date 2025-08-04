import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient

from api.api_v1.films.crud import storage
from main import app
from schemas.movie import DESCRIPTION_MAX_LENGTH, Movie
from tests.conftest import create_movie


class TestUpdatePartial:

    @pytest.fixture()
    def movie(self, request: SubRequest) -> Movie:
        slug, description = request.param
        return create_movie(
            slug=slug,
            description=description,
        )

    @pytest.mark.parametrize(
        "movie, new_description",
        [
            pytest.param(
                ("foo", "a description"),
                "",
                id="foo",
            ),
            pytest.param(
                ("bar", "b description"),
                "some description",
                id="bar",
            ),
            pytest.param(
                ("max_tomin", "a" * DESCRIPTION_MAX_LENGTH),
                "",
                id="max-description-to-max-description",
            ),
            pytest.param(
                ("min-to-max", ""),
                "a" * DESCRIPTION_MAX_LENGTH,
                id="no-description-to-max-description",
            ),
        ],
        indirect=["movie"],
    )
    def test_update_movie_details_partial(
        self,
        movie: Movie,
        new_description: str,
        auth_client: TestClient,
    ) -> None:
        url = app.url_path_for(
            "update_partial_details",
            slug=movie.slug,
        )

        response = auth_client.patch(
            url,
            json={"description": new_description},
        )

        assert response.status_code == status.HTTP_200_OK, response.text
        movie_db = storage.get_by_slug(movie.slug)
        assert movie_db.description == new_description
