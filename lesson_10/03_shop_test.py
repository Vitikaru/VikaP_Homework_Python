import allure
from selenium import webdriver
from pages_shop.Authorization import Authorization
from pages_shop.AddingProduct import AddingProduct
from pages_shop.FillingForm import FillingForm
from pages_shop.Witing import Witing


@allure.title("Интернет-магазин")
@allure.description("Оформить заказ")
@allure.feature("READ")
@allure.severity("blocker")
def test_shop():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome()
    
    autho = Authorization(browser)
    autho.autho("standard_user", "secret_sauce")


    add = AddingProduct(browser)
    add.add()
    
    form = FillingForm(browser)
    form.form("Виктория", "Пржанова", "628301")
    
    wait = Witing(browser)
    wait.waiting_text()

    browser.quit()
