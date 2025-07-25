from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client() -> Generator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client
