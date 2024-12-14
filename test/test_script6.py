from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
def configurar_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

# Función para iniciar sesión
def iniciar_sesion(driver, url, username, password):
    try:
        print("Iniciando la prueba de inicio de sesión...")

        # Navegar a la URL
        driver.get(url)

        # Esperar a que el campo de usuario esté presente y rellenarlo
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login_field")))
        usuario = driver.find_element(By.ID, "login_field")
        usuario.send_keys(username)

        # Esperar a que el campo de contraseña esté presente y rellenarlo
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        contrasena = driver.find_element(By.ID, "password")
        contrasena.send_keys(password)

        # Esperar a que el botón de inicio de sesión esté presente y hacer clic
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "commit")))
        boton_login = driver.find_element(By.NAME, "commit")
        boton_login.click()

        # Verificar si la página redirige correctamente tras el inicio de sesión
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//summary[@aria-label='View profile and more']"))
            )
            print("Inicio de sesión exitoso. Usuario redirigido a la página principal.")
        except TimeoutException:
            # Si no redirige, verificar el mensaje de error
            mensaje_error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'flash-error') or @class='flash flash-full flash-error ']"))
            )
            print("Mensaje de error: ", mensaje_error.text)

    except NoSuchElementException as e:
        print(f"Error: No se encontró un elemento. Detalles del error: {e}")
    except TimeoutException as e:
        print(f"Error: La operación tomó demasiado tiempo. Detalles del error: {e}")
    except Exception as e:
        print(f"Error: Ocurrió un error inesperado. Detalles del error: {e}")
    finally:
        # Pausa para observar los resultados antes de cerrar el navegador
        time.sleep(5)
        driver.quit()
        print("Prueba de inicio de sesión finalizada.")

# Función principal
def main():
    driver = configurar_driver()
    url = "https://github.com/login"
    username = "usuario_falso"
    password = "contraseña_falsa"

    iniciar_sesion(driver, url, username, password)

if __name__ == "__main__":
    main()
