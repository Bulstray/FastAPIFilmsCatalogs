# FastAPI Films Catalog

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)

## CI/CD Status

[![Black](https://img.shields.io/badge/Black-◼️_Format-000000?style=flat-square&logo=python&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Ruff](https://img.shields.io/badge/Ruff-🪶_Lint-FCC21B?style=flat-square&logo=python&logoColor=black)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![MyPy](https://img.shields.io/badge/MyPy-🧪_Types-0075C9?style=flat-square&logo=python&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Pytest](https://img.shields.io/badge/Pytest-🧪_Tests-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Coverage](https://img.shields.io/badge/Codecov-📊_Coverage-F01F7A?style=flat-square&logo=codecov&logoColor=white)](https://codecov.io/gh/Bulstray/FastAPIFilmsCatalogs)

## Workflow Status

[![Python Checks](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yml/badge.svg?style=flat-square)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Tests](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yml/badge.svg?event=pull_request&style=flat-square)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
## Develop

Check GitHub Actions after any push.

### Setup

Right click 'films-catalog' -> Mark Directory as -> Source root

### Configure pre-commit

### Install dependencies

Install all packages
```shell
uv sync
```

Install pre-commit hook:
```shell
pre-commit intall
```


### Install

Install packages:
```shell
uv install
```

### Run

Go to workdir:
```shell
cd films-catalog
```

Run dev server:
```shell
fastapi dev
```
