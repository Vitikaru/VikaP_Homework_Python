import allure
from selenium.webdriver.common.by import By


class Form:
    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step("Заполнение полей данными")
    def cearh(
            self, first_name, last_name,
            address, e_mail, phone,
            city, country, job_position, company
            ):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]'
                                 ).send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]'
                                 ).send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]'
                                 ).send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]'
                                 ).send_keys(e_mail)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]'
                                 ).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]'
                                 ).send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]'
                                 ).send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]'
                                 ).send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]'
                                 ).send_keys(company)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]'
                                 ).click()
