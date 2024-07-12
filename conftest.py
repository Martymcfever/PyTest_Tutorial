import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, ProductFactory
from selenium import webdriver

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)

@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create ()
    return user


@pytest.fixture(scope='class')
def chrome_driver_init(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options = options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.fixture(params= ["chrome", "firefox"], scope= "class")
def driver_init(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(options = options)
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(options = options)

    request.cls.driver = web_driver
    yield
    web_driver.close()
