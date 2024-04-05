import pytest


@pytest.fixture
def a():
    return 'aaa'

@pytest.fixture
def b():
    return 'bbb'

@pytest.fixture(params=['a', 'b'])
def arg(request):
    return request.getfixturevalue(request.param)