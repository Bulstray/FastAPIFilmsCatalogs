# FastAPI Films Catalog

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

## CI/CD Status

[![Black](https://img.shields.io/badge/Black-◼️_Code_Format-000000?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Ruff](https://img.shields.io/badge/Ruff-🪶_Linting-FCC21B?style=for-the-badge&logo=python&logoColor=black)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![MyPy](https://img.shields.io/badge/MyPy-🧪_Type_Checking-0075C9?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Pytest](https://img.shields.io/badge/Pytest-🧪_Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Coverage](https://img.shields.io/badge/Codecov-📊_Coverage-F01F7A?style=for-the-badge&logo=codecov&logoColor=white)](https://codecov.io/gh/Bulstray/FastAPIFilmsCatalogs)

## Workflow Badges

![Python Checks](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yml/badge.svg?style=for-the-badge)
![Tests](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yml/badge.svg?event=pull_request&style=for-the-badge)
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
