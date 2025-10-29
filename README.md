# FastAPI Films Catalog

## 🛠 Quality Assurance

| Tool | Status | Purpose |
|------|--------|---------|
| **Black** | ![Black](https://img.shields.io/badge/◼️_Black-Formatted-000000?style=flat-square) | Code formatting |
| **Ruff** | ![Ruff](https://img.shields.io/badge/🪶_Ruff-Linting-FCC21B?style=flat-square&logoColor=black) | Code linting |
| **MyPy** | ![MyPy](https://img.shields.io/badge/🧪_MyPy-Typing-0075C9?style=flat-square) | Type checking |
| **Pytest** | ![Pytest](https://img.shields.io/badge/🧪_Pytest-Testing-0A9EDC?style=flat-square) | Test execution |
| **Coverage** | ![Coverage](https://img.shields.io/badge/📊_Coverage-Reports-F01F7A?style=flat-square) | Code coverage |

## 📊 CI/CD Status

[![Python Checks](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions/workflows/python-checks.yml/badge.svg)](https://github.com/Bulstray/FastAPIFilmsCatalogs/actions)
[![Codecov](https://codecov.io/gh/Bulstray/FastAPIFilmsCatalogs/branch/master/graph/badge.svg)](https://codecov.io/gh/Bulstray/FastAPIFilmsCatalogs)
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
