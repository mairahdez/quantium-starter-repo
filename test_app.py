import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_app_elements():
   
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
   
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        
        driver.get("http://127.0.0.1:8050")
        
        wait = WebDriverWait(driver, 10)
        
  
        h1 = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        assert "Soul Foods" in h1.text, f"Se esperaba 'Soul Foods' pero se obtuvo: {h1.text}"
        
        chart = wait.until(EC.visibility_of_element_located((By.ID, "sales-line-chart")))
        assert chart.is_displayed(), "El gráfico 'sales-line-chart' no está visible."        
        
        print("\n¡Prueba pasada con éxito!")
        
    finally:
        driver.quit()