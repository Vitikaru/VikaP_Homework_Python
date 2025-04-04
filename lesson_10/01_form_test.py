import allure
from selenium import webdriver
from pages_form.Form import Form
from pages_form.ColorCheck import ColorCheck


@allure.title("Форма")
@allure.description("Заполненить форму")
@allure.feature("READ")
@allure.severity("blocker")
def test_form():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome()

    form = Form(browser)
    form.cearh(
        "Иван", "Петров", "Ленина, 55-3",
        "test@skypro.com", "+7985899998787", "Москва",
        "Россия", "QA", "SkyPro")

    color = ColorCheck(browser)
    color.color_check_red()
    color.color_check_green()

    browser.quit()
