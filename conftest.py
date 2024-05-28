import pytest
from selenium import webdriver
from generators import AuthGenerator


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService(executable_path='/Users/serg/Gprojects/qa_python_sprint_5/chromedriver')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def generated_user():
    generated_user = AuthGenerator()
    generated_user.login = generated_user.login_generator()
    generated_user.password = generated_user.correct_password_generator()
    yield generated_user


@pytest.fixture(scope='function')
def fixed_user():
    fixed_user = AuthGenerator()
    fixed_user.login = "sergeychetverousfs06827@yandex.ru"
    fixed_user.password = "qknA9E"
    yield fixed_user
