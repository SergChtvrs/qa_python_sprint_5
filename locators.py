from selenium.webdriver.common.by import By


class Locators:
    SEARCH_ACCOUNT_BUTTON = By.XPATH, "//a[@href='/account']"  # кнопка Личный кабинет в шапке
    SEARCH_REGISTER_REFERENCE = By.XPATH, "//a[@href='/register']"  # ссылка Регистрация странице входа в ЛК
    SEARCH_NAME_FIELD_ON_REG_PAGE = By.XPATH, "//*[text()='Имя']/parent::*/input"  # поле Имя на странице регистрации
    SEARCH_EMAIL_FIELD_ON_REG_PAGE = By.XPATH, "//*[text()='Email']/parent::*/input"  # поле Email на странице регистрации
    SEARCH_PASSWORD_FIELD = By.NAME, "Пароль"  # поле Пароль
    SEARCH_EMAIL_FIELD = By.NAME, "name"  # поле Имя на странице входа
    SEARCH_PURPLE_BUTTON = By.XPATH, "//*[contains(@class, 'button_button_type_primary')]"  # фиолетовая кнопка
    SEARCH_ERROR_TEXT = By.CLASS_NAME, "input__error" # текст ошибки
    SEARCH_FORGOT_PASSWORD_REFERENCE_ON_LOGIN_PAGE = By.XPATH, "//a[@href='/forgot-password']"  # ccлылка Восстановление пароля на странице входа
    SEARCH_LOGIN_REFERENCE_ON_REGISTER_PAGE = By.XPATH, "//a[@href='/login']" # ccлылка Вход на странице регистрации
    SEARCH_CONSTRUCTOR_BUTTON = By.XPATH, ("//*[(contains(@class,"
                                           " 'AppHeader_header__link')) and @href='/']")  # кнопка Конструктор в шапке
    SEARCH_HEADER_LOGO = By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]" # логотип в шапке
    SEARCH_EXIT_BUTTON = By.XPATH, "//*[text()='Выход']" # кнопка Выход в личном кабинете
    SEARCH_TEXT_ON_LOGIN_PAGE = By.XPATH, "//*[text()='Вход']"  # текст Вход
    SEARCH_CONSTRUCTOR_MENU_TEXT_BUN = (By.XPATH,
                                        "//*[contains(@class,'BurgerIngredients_ingredients')]/child::h2[text()='Булки']")  # Текст Булки в меню конструктора
    SEARCH_CONSTRUCTOR_MENU_TEXT_SAUCE = (By.XPATH,
                                          "//*[contains(@class,'BurgerIngredients_ingredients')]/child::h2[text()='Соусы']")  # Текст Соусы в меню конструктора
    SEARCH_CONSTRUCTOR_MENU_TEXT_FILLING = (By.XPATH,
                                            "//*[contains(@class,'BurgerIngredients_ingredients')]/child::h2[text()='Начинки']")  # Текст Начинки в меню конструктора
    SEARCH_CONSTRUCTOR_BUN_TAB = (By.XPATH,
                                  "//*[contains(@class,'BurgerIngredients_ingredients')]/descendant::span[text()='Булки']/parent::*")   # Таб Булки конструктора
    SEARCH_CONSTRUCTOR_SAUCE_TAB = (By.XPATH,
                                    "//*[contains(@class,'BurgerIngredients_ingredients')]/descendant::span[text()='Соусы']/parent::*")   # Таб Соусы конструктора
    SEARCH_CONSTRUCTOR_FILLING_TAB = (By.XPATH,
                                      "//*[contains(@class,'BurgerIngredients_ingredients')]/descendant::span[text()='Начинки']/parent::*")  # Таб Начинки конструктора




