import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage
from pages.sandbox_page import SandboxPage

BASE_URL = "https://www.saucedemo.com/"
DEFAULT_PASSWORD = "secret_sauce"

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService())
    yield driver
    driver.quit()

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)

# Fixtures por usuario
@pytest.fixture
def standard_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("standard_user", DEFAULT_PASSWORD)

@pytest.fixture
def locked_out_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("locked_out_user", DEFAULT_PASSWORD)

@pytest.fixture
def problem_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("problem_user", DEFAULT_PASSWORD)

@pytest.fixture
def visual_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("visual_user", DEFAULT_PASSWORD)

@pytest.fixture
def performance_glitch_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("performance_glitch_user", DEFAULT_PASSWORD)

@pytest.fixture
def error_user_page(login_page):
    login_page.navigate_sauce_demo()
    return login_page.login_user("error_user", DEFAULT_PASSWORD)
