from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


main_page_link = "https://stellarburgers.nomoreparties.site/"


class TestConstructor:
    def test_move_to_sauce(self, driver):
        # открываем главную страницу
        driver.get(main_page_link)
        # нажимаем на таб
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_TAB_SAUCE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_SAUCE))
        tab_text = driver.find_element(*Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_SAUCE).text
        # проверяем, что раздел меню корректный
        assert tab_text == "Соусы", \
            f'Текст раздела меню не соответвует табу: {tab_text} != Соусы'

    def test_move_to_filling(self, driver):
        # открываем главную страницу
        driver.get(main_page_link)
        # нажимаем на таб
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_TAB_FILLING).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_FILLING))
        tab_text = driver.find_element(*Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_FILLING).text
        # проверяем, что раздел меню корректный
        assert tab_text == "Начинки", \
            f'Текст раздела меню не соответвует табу: {tab_text} != Начинки'

    def test_move_to_bun(self, driver):
        # открываем главную страницу
        driver.get(main_page_link)
        # нажимаем на таб соусов
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_TAB_SAUCE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_SAUCE))
        # нажимаем на таб булок
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_TAB_BUN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_BUN))
        tab_text = driver.find_element(*Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_BUN).text
        # проверяем, что раздел меню корректный
        assert tab_text == "Булки", \
            f'Текст раздела меню не соответвует табу: {tab_text} != Булки'
