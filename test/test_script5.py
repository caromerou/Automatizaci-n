from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Configurar el WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navegar a Wikipedia
driver.get("https://www.wikipedia.org/")

# Esperar a que la página cargue
time.sleep(2)

# Encontrar el campo de búsqueda usando su nombre (name)
search_box = driver.find_element(By.NAME, "search")

# Escribir texto en el campo de búsqueda
search_box.send_keys("Selenium (software)")

# Enviar el formulario (hacer una búsqueda)
search_box.submit()

# Esperar a que la página de resultados cargue
time.sleep(2)

# Obtener el primer párrafo del artículo
first_paragraph = driver.find_element(By.XPATH, "//div[@class='mw-parser-output']/p[1]")
print(first_paragraph.text)

# Cerrar el navegador
driver.quit()
