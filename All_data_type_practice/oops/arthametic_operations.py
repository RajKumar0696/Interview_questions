import pytest


@pytest.fixture()
def add_of(x, y):
    return x + y


def mul_of(x, y):
    return x * y


@pytest.yield_fixture()
def dev_of(x, y):
    if y != 0:
        return x / y


def subtract(x, y):
    return x - y


print(add_of(10, 20))
print(dev_of(10, 20))
print(mul_of(10, 20))
print(subtract(10, 20))
