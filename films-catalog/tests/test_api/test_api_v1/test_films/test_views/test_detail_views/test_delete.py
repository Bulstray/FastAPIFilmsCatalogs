import pytest
from _pytest.fixtures import SubRequest
from fastapi import status
from fastapi.testclient import TestClient

from api.api_v1.films.crud import storage
from main import app
from schemas.movie import Movie, MovieCreate


def create_movie(slug: str) -> Movie:
    movie = MovieCreate(
        slug=slug,
        description="some description",
        name="some name",
    )
    return storage.create(movie)


@pytest.fixture(
    params=[
        "some slug",
        "slug",
        "qwertyabc",
        pytest.param("abc", id="minimal-slug"),
        pytest.param("qwerty-foo", id="max-slug"),
    ],
)
def movie(request: SubRequest) -> Movie:
    return create_movie(request.param)


def test_delete(
    movie: Movie,
    auth_client: TestClient,
) -> None:

    url = app.url_path_for(
        "delete_movie",
        slug=movie.slug,
    )
    response = auth_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
    assert not storage.exists(movie.slug)
