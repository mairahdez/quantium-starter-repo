import pytest
from dash.testing.browser import Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def dash_br(request):
    """
    Configura el driver para que descargue e instale la versión correcta automáticamente.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    
    driver = webdriver.Chrome(service=service, options=options)
    browser = Browser(driver, "chrome")
    
    yield browser
    browser.driver.quit()