from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


main_page_link = "https://stellarburgers.nomoreparties.site/"
account_page = "https://stellarburgers.nomoreparties.site/account/profile"
login_page_link = "https://stellarburgers.nomoreparties.site/login"


class TestClickOnExitButton:
    def test_authorized_user_move_to_login_page_by_click_on_exit_button(self, driver, fixed_user):
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
        # кликаем по кнопке Выход
        driver.find_element(*Locators.SEARCH_EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_TEXT_ON_LOGIN_PAGE))
        # проверяем, что находимся на странице авторизации
        assert driver.current_url == login_page_link, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {login_page_link}'
