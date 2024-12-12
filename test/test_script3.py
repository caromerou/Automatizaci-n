import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Inicializar el navegador
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navegar a la página de formularios de demoqa
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(3)  # Pausa para ver la página inicial

    # Llenar campos de texto
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Juan")
    time.sleep(2)  # Pausa para ver la entrada del primer nombre

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Pérez")
    time.sleep(2)  # Pausa para ver la entrada del apellido

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("juan.perez@example.com")
    time.sleep(2)  # Pausa para ver la entrada del correo electrónico

    # Seleccionar un radio button
    gender_radio = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    gender_radio.click()
    time.sleep(2)  # Pausa para ver la selección del género

    phone = driver.find_element(By.ID, "userNumber")
    phone.send_keys("1234567890")
    time.sleep(2)  # Pausa para ver la entrada del teléfono

    # Seleccionar una fecha en el datepicker
    dob_input = driver.find_element(By.ID, "dateOfBirthInput")
    dob_input.click()
    time.sleep(2)
    select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    select_month.select_by_visible_text("May")
    select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    select_year.select_by_visible_text("1990")
    driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--012']").click()
    time.sleep(2)

    # Llenar Subjects
    subjects_input = driver.find_element(By.ID, "subjectsInput")
    subjects_input.send_keys("Computer Science")
    subjects_input.send_keys(Keys.RETURN)
    time.sleep(2)

    # Seleccionar un checkbox
    hobbies_checkbox = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
    hobbies_checkbox.click()
    time.sleep(2)  # Pausa para ver la selección del hobby

    # Subir un archivo
    upload_file = driver.find_element(By.ID, "uploadPicture")
    upload_file.send_keys("/path/to/your/file.png")  # Reemplaza con la ruta a tu archivo
    time.sleep(2)

    # Llenar dirección
    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("Calle Falsa 123")
    time.sleep(2)

    # Seleccionar estado y ciudad
    state_dropdown = driver.find_element(By.ID, "react-select-3-input")
    state_dropdown.send_keys("NCR")
    state_dropdown.send_keys(Keys.RETURN)
    time.sleep(2)

    city_dropdown = driver.find_element(By.ID, "react-select-4-input")
    city_dropdown.send_keys("Delhi")
    city_dropdown.send_keys(Keys.RETURN)
    time.sleep(2)

    # Enviar el formulario
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)  # Pausa para ver la acción de envío

    print("El formulario se llenó y envió correctamente.")

finally:
    # Cerrar el navegador
    driver.quit()
