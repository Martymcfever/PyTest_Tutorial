import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, ProductFactory

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create ()
    return user





