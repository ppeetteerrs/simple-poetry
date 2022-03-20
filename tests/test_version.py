import pytest
import simple_pypackage


@pytest.fixture
def version():
    return simple_pypackage.__version__


def test_version(version: str):
    assert version is not None
