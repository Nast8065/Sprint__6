import pytest
from selenium import webdriver
from helpers.data import Urls

@pytest.fixture
def driver():
#Фикстура для создания и закрытия драйвера Firefox
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

# Для корректного отображения аргументов в параметризированном тесте
def pytest_make_parametrize_id(val):
    return repr(val)
