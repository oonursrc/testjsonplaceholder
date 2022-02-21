import pytest


@pytest.fixture(scope='session')
def context():
    return {}
