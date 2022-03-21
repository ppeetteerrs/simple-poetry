import pytest
import simple_poetry


@pytest.fixture
def version():
    return simple_poetry.__version__


def test_version(version: str):
    assert version is not None
