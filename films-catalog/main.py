from typing import Annotated

import uvicorn
from fastapi import FastAPI, Request, Depends, HTTPException, status

from schemas.film import Film

app = FastAPI(title="Films Catalog")


@app.get("/")
def read_docs(request: Request):
    docs_url = request.url.replace(
        path="/docs",
    )

    return {"docs": str(docs_url)}


FILMS = [
    Film(
        movie_id=1,
        name="Остров проклятых",
        description="Фильм про психбольницу",
    ),
    Film(
        movie_id=2,
        name="Джентельмены",
        description="Фильм про мафию",
    ),
    Film(
        movie_id=3,
        name="Область тьмы",
        description="Фильм про работу мозга",
    ),
]


@app.get(
    "/films/",
    response_model=list[Film],
)
def read_film_list():
    return FILMS


def prefetch_film_by_id(movie_id: int) -> Film:
    film: Film | None = next(
        (film for film in FILMS if film.movie_id == movie_id),
        None,
    )

    if film:
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {movie_id!r} not found",
    )


@app.get("/film/{movie_id}")
def get_film_by_id(
    film: Annotated[
        Film,
        Depends(prefetch_film_by_id),
    ],
):
    return film


if __name__ == "__main__":
    uvicorn.run(app)
