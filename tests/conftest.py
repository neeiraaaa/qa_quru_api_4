import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.demoqa_with_env import DemoQaWithEnv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def demoshop(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def cookie(demoshop):
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    return authorization_cookie


@pytest.fixture(scope='function')
def app(demoshop, cookie):
    browser.config.base_url = demoshop.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def reqres(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env).session_reqres
