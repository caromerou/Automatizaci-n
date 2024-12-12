from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Usar WebDriver Manager para manejar el chromedriver automáticamente
service = Service(ChromeDriverManager().install())

# Inicializar el navegador con el servicio
driver = webdriver.Chrome(service=service)

# Abre una página de prueba
driver.get('https://www.google.com')

# Cierra el navegador
driver.quit()
