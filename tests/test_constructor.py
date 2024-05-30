from locators import Locators
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:
    def test_move_to_sauce(self, driver):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # нажимаем на таб
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_SAUCE_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_SAUCE))
        assert "tab_tab_type_current" in driver.find_element(
            *Locators.SEARCH_CONSTRUCTOR_SAUCE_TAB).get_attribute("class")

    def test_move_to_filling(self, driver):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # нажимаем на таб
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_FILLING_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_FILLING))
        assert "tab_tab_type_current" in driver.find_element(
            *Locators.SEARCH_CONSTRUCTOR_FILLING_TAB).get_attribute("class")

    def test_move_to_bun(self, driver):
        # открываем главную страницу
        driver.get(Urls.LINK)
        # нажимаем на таб начинок
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_FILLING_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_FILLING))
        # нажимаем на таб булок
        driver.find_element(*Locators.SEARCH_CONSTRUCTOR_BUN_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.SEARCH_CONSTRUCTOR_MENU_TEXT_BUN))
        assert "tab_tab_type_current" in driver.find_element(
            *Locators.SEARCH_CONSTRUCTOR_BUN_TAB).get_attribute("class")

