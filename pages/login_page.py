from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.example.com/login"

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, "username")  # Cambia según el nombre del campo en la página
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")  # Cambia según el nombre del campo en la página
        password_field.send_keys(password)

    def submit(self):
        password_field = self.driver.find_element(By.NAME, "password")  # Cambia según el nombre del campo
        password_field.send_keys(Keys.RETURN)
