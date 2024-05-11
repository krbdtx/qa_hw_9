import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 750
    browser.config.window_width = 1200

    yield
    browser.quit()