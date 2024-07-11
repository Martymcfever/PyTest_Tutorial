import pytest
from django.contrib.auth.models import User

# #arrange step
# @pytest.fixture()
# def user1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     #act step
#     user_1.set_password("new-password")
#     #assert step
#     assert user_1.check_password("new-password") is True


# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     return user


# def test_set_check_password1(user_1):
#     assert user_1.username == "test-user"






# def test_set_check_password_1(user_2):
#     print("Check User 1")
#     assert user_2.username == "test-user"

# def test_set_check_password_2(user_2):
#     print("Check User 2")
#     assert user_2.username == "test-user"


# def test_new_user(user_B):
#     print(user_B.is_staff)
#     assert user_B.is_staff

@pytest.mark.django_db
def test_new_user(user_factory):
    user = user_factory.build()
    #count = User.objects.all().count()
    #print(count)
    print(user.username)
    assert user.username != ""

def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert product.description != ""