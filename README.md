# 🎬 FastAPI Films Catalog

[![Python checks 🐍](https://img.shields.io/github/actions/workflow/status/bulstray/FastAPIFilmsCatalogs/python-checks.yaml?branch=master&label=Python%20checks%20%F0%9F%90%8D&logo=github&style=for-the-badge)](https://github.com/bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yaml)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&style=for-the-badge)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&style=for-the-badge)](https://github.com/psf/black)
[![Lint: Ruff](https://img.shields.io/badge/lint-ruff-%23efc000?logo=ruff&logoColor=white&style=for-the-badge)](https://github.com/astral-sh/ruff)
[![Type Checking: mypy](https://img.shields.io/badge/type%20checking-mypy-blueviolet?logo=python&style=for-the-badge)](https://github.com/python/mypy)
[![Dependency: uv](https://img.shields.io/badge/dependencies-uv-4B8BBE?logo=python&style=for-the-badge)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-22C55E?style=for-the-badge&logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/bulstray/2ad8288ac28a410072f6d112f470bf61/raw/coverage.json&style=for-the-badge)](./.github/workflows/python-checks.yaml)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/bulstray/FastAPIFilmsCatalogs/master.svg)](https://results.pre-commit.ci/latest/github/bulstray/FastAPIFilmsCatalogs/master)
[![Codecov](https://codecov.io/gh/bulstray/FastAPIFilmsCatalogs/branch/master/graph/badge.svg)](https://codecov.io/gh/bulstray/FastAPIFilmsCatalogs)

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
