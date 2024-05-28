from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


main_page_link = "https://stellarburgers.nomoreparties.site/"


class TestLogin:
    def test_user_should_login_successfully_by_button_on_main_page(self, driver, fixed_user):
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
        # проверям, что имя пользователя в личном кабинете соответстует имени зарегистрированного пользователя
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == fixed_user.login

    def test_user_should_login_successfully_by_account_button_in_header(self, driver, fixed_user):
        # открываем главную страницу
        driver.get(main_page_link)
        # переходим на страницу личного кабинета
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
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
        # проверям, что имя пользователя в личном кабинете соответстует имени зарегистрированного пользователя
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == fixed_user.login

    def test_user_should_login_successfully_by_button_on_register_page(self, driver, fixed_user):
        # открываем главную страницу
        driver.get(main_page_link)
        # переходим на страницу личного кабинета
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        # переходим на страницу регистрации
        driver.find_element(*Locators.SEARCH_REGISTER_REFERENCE).click()
        # переходим на страницу входа
        driver.find_element(*Locators.SEARCH_LOGIN_REFERENCE_ON_REGISTER_PAGE).click()
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
        # проверям, что имя пользователя в личном кабинете соответстует имени зарегистрированного пользователя
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == fixed_user.login

    def test_user_should_login_successfully_by_button_on_forgot_password_page(self, driver, fixed_user):
        # открываем главную страницу
        driver.get(main_page_link)
        # переходим на страницу личного кабинета
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        # переходим на страницу восстановления пароля кабинета
        driver.find_element(*Locators.SEARCH_FORGOT_PASSWORD_REFERENCE_ON_LOGIN_PAGE).click()
        # переходим на страницу входа
        driver.find_element(*Locators.SEARCH_LOGIN_REFERENCE_ON_REGISTER_PAGE).click()
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
        # проверям, что имя пользователя в личном кабинете соответстует имени зарегистрированного пользователя
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == fixed_user.login
