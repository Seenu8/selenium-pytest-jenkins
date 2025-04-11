from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google_title(setup):
    setup.get("https://www.google.com")
    assert "Google" in setup.title
