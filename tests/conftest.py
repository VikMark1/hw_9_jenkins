import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_prep():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    yield