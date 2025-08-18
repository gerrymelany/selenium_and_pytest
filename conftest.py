# conftest.py
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from pages.sandbox_page import SandboxPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on, option: chrome, firefox, edge")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService())
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported. Choose from 'chrome', 'firefox', 'edge'.")
    yield driver
    driver.quit()

@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)