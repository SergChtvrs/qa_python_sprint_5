from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


main_page_link = "https://stellarburgers.nomoreparties.site/"
account_page = "https://stellarburgers.nomoreparties.site/account/profile"


class TestClickOnConstructorButton:
    def test_authorized_user_move_to_main_page_by_click_on_constructor_button(self, driver, fixed_user):
        # открываем главную страницу
        driver.get(main_page_link)
        # переходим на страницу авторизации
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        # авторизуемся
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(fixed_user.login)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(fixed_user.password)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        # переходим в личный кабинет
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        # проверяем, что мы на странице пользователя
        assert driver.current_url == account_page, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {account_page}'
        # кликаем по кнопке Конструктор
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_BUTTON).click()
        # проверяем, что находимся на главной странице
        assert driver.current_url == main_page_link, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {main_page_link}'

    def test_authorized_user_move_to_main_page_by_click_on_header_logo(self, driver, fixed_user):
        # открываем главную страницу
        driver.get(main_page_link)
        # переходим на страницу авторизации
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        # авторизуемся
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(fixed_user.login)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(fixed_user.password)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        # переходим в личный кабинет
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        # проверяем, что мы на странице пользователя
        assert driver.current_url == account_page, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {account_page}'
        # кликаем по кнопке Конструктор
        driver.find_element(*Locators.SEARCH_HEADER_LOGO).click()
        # проверяем, что находимся на главной странице
        assert driver.current_url == main_page_link, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {main_page_link}'
