import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# Example 1: Initial Test with browser pop up

# class TestBrowser1(LiveServerTestCase):
#     def test_examples(self):
#         driver = webdriver.Chrome()
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title


# Example 2: Same as last test but without the window poping up

# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(options = options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title


# Example 3: Integrating PyTest

# @pytest.fixture(scope='class')
# def chrome_driver_init(request):

#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chrome_driver = webdriver.Chrome(options = options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()

# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title


# Example 4: Utilize both Chrome and Firefox

# @pytest.fixture(params= ["chrome", "firefox"], scope= "class")
# def driver_init(request):
#     if request.param == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Chrome(options = options)
#     if request.param == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         web_driver = webdriver.Firefox(options = options)

#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title