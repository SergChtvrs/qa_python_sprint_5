from locators import Locators
from data import FixedUser
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestClickOnAccountButton:
    def test_unauthorized_user_move_to_login_page_by_click_on_account_button(self, driver):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # переходим на страницу авторизации
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        # проверяем, что мы на странице авторизации
        assert driver.current_url == Urls.LOGIN_PAGE, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {Urls.LOGIN_PAGE}'

    def test_authorized_user_move_to_account_page_by_click_on_account_button(self, driver):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # переходим на страницу авторизации
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        # авторизуемся
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
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
        assert driver.current_url == Urls.ACCOUNT_PAGE, \
            f'текущий url не соответствует ожидаемому: {driver.current_url} != {Urls.ACCOUNT_PAGE}'
