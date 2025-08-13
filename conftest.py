# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.sandbox_page import SandboxPage

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService())
    yield driver
    driver.quit()

@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)