import pytest
from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegister:
    def test_user_register_successfully_with_correct_password_length(self, driver, generated_user):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # переходим на форму регистрации
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.SEARCH_REGISTER_REFERENCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_NAME_FIELD_ON_REG_PAGE))
        # заполняем форму
        driver.find_element(*Locators.SEARCH_NAME_FIELD_ON_REG_PAGE).send_keys(generated_user.user_name)
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD_ON_REG_PAGE).send_keys(generated_user.login)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(generated_user.password)
        # нажимаем Зарегистрироваться
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Войти"))
        # Авторизуемся
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD).send_keys(generated_user.login)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(generated_user.password)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.SEARCH_PURPLE_BUTTON, "Оформить заказ"))
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_EMAIL_FIELD))
        # проверям, что имя пользователя в личном кабинете соответстует имени зарегистрированного пользователя
        assert driver.find_element(*Locators.SEARCH_EMAIL_FIELD).get_attribute("value") == generated_user.login

    @pytest.mark.parametrize('password_length', [3, 5],
                             ids=['длина пароль 3 символа', 'длина пароля 5 симоволов'])
    def test_user_register_failed_with_incorrect_password_length(self, driver, generated_user, password_length):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # переходим на форму регистрации
        driver.find_element(*Locators.SEARCH_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.SEARCH_REGISTER_REFERENCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_NAME_FIELD_ON_REG_PAGE))
        # заполняем форму
        driver.find_element(*Locators.SEARCH_NAME_FIELD_ON_REG_PAGE).send_keys(generated_user.user_name)
        driver.find_element(*Locators.SEARCH_EMAIL_FIELD_ON_REG_PAGE).send_keys(generated_user.login)
        driver.find_element(*Locators.SEARCH_PASSWORD_FIELD).send_keys(generated_user.password[0:password_length])
        # нажимаем Зарегистрироваться
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.SEARCH_PURPLE_BUTTON))
        driver.find_element(*Locators.SEARCH_PURPLE_BUTTON).click()
        # проверяем ошибку
        assert driver.find_element(*Locators.SEARCH_ERROR_TEXT).text == "Некорректный пароль", \
            'ошибка авторизации не обнаружена или некорректный текст ошибки'
