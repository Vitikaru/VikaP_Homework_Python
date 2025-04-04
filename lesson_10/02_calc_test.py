import allure
from pages_calc.Calkulator import Calkulator
from selenium import webdriver


@allure.title("Калькулятор")
@allure.description("Выполнить арифметический расчет")
@allure.feature("READ")
@allure.severity("blocker")
def test_calc():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome()

    calc = Calkulator(browser)
    with allure.step("Проверка времени ожидания"):
        calc.calc("45")
    
    browser.quit()
