import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar el WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navegar a la página de registro de DemoQA
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# Rellenar el nombre y el apellido
driver.find_element(By.ID, "firstName").send_keys("Juan")
driver.find_element(By.ID, "lastName").send_keys("Pérez")

# Rellenar el correo electrónico
driver.find_element(By.ID, "userEmail").send_keys("juan.perez@example.com")

# Seleccionar el género
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()

# Rellenar el número de teléfono
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

# Seleccionar la fecha de nacimiento
driver.find_element(By.ID, "dateOfBirthInput").click()
select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
select_month.select_by_visible_text("May")
select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
select_year.select_by_visible_text("1990")
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--012')]").click()

# Rellenar las asignaturas
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("Maths")
subject_input.send_keys(Keys.RETURN)

# Seleccionar hobbies
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()

# Subir una foto
driver.find_element(By.ID, "uploadPicture").send_keys("/ruta/a/tu/archivo/foto.png")

# Rellenar la dirección
driver.find_element(By.ID, "currentAddress").send_keys("Calle Falsa 123, Ciudad Ficticia")

# Seleccionar estado y ciudad
driver.find_element(By.ID, "state").click()
state_option = driver.find_element(By.XPATH, "//div[contains(text(), 'NCR')]")
state_option.click()

driver.find_element(By.ID, "city").click()
city_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Delhi')]")
city_option.click()

# Enviar el formulario
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Cerrar el navegador
driver.quit()
