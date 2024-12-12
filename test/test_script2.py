import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Usar WebDriver Manager para manejar el chromedriver automáticamente
service = Service(ChromeDriverManager().install())

# Inicializar el navegador con el servicio
driver = webdriver.Chrome(service=service)

try:
    # Navegar a Google
    driver.get("https://www.google.com")

    # Buscar algo en Google
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    # Esperar a que se carguen los resultados
    time.sleep(5)

    # Verificar que "Selenium WebDriver" está en el título de la página
    assert "Selenium WebDriver" in driver.title

    print("La prueba fue exitosa, los resultados de búsqueda se mostraron correctamente.")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar el navegador
    driver.quit()
