from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver, self.url = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#user-name")))

    def check_login_input(self):
        login = self.driver.find_element(By.CSS_SELECTOR, "input#user-name")
        return login
