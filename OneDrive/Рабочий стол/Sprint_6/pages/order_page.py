import allure
import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementClickInterceptedException, 
    ElementNotInteractableException, 
    StaleElementReferenceException,
    TimeoutException,
    NoSuchElementException,
    WebDriverException
)

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

#Page Object для страницы заказа самоката

    @allure.step('Заполнение поля Имя')
    def send_name_to_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.name_field, text)

    @allure.step('Заполнение поля Фамилия')
    def send_last_name_to_last_name_field(self, text):
        self.send_keys_to_field(OrderPageLocators.last_name_field, text)

    @allure.step('Заполнение поля Адрес')
    def send_address_to_address_field(self, text):
        self.send_keys_to_field(OrderPageLocators.address_field, text)

    @allure.step('Заполнение поля Станция метро')
    def send_metro_station_to_metro_station_field(self, text):
        # Кликаем на поле станции метро
        self.click_button(OrderPageLocators.metro_station_field)
        # Очищаем поле и вводим текст
        element = self.find_and_wait_locator(OrderPageLocators.metro_station_field)
        element.clear()
        element.send_keys(text)
        # Ждем появления выпадающего списка и кликаем на нужную станцию
        self.wait_for_element_clickable(OrderPageLocators.metro)
        self.click_button(OrderPageLocators.metro)

    @allure.step('Заполнение поля Номер телефона')
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys_to_field(OrderPageLocators.telephone_field, text)

    @allure.step('Клик на кнопку Далее')
    def click_on_the_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('''Заполнение данных на странице "Для кого самокат"
                                 и переход на сл.страницу "Про аренду"''')
    def complete_filling_of_the_who_is_scooter_form(self, user):
        try:
            self.send_name_to_name_field(user[1])
            self.send_last_name_to_last_name_field(user[2])
            self.send_address_to_address_field(user[3])
            self.send_metro_station_to_metro_station_field(user[4])
            self.send_telephone_number_to_telephone_number_field(user[5])
            self.click_on_the_next_button()
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
            # Если возникла ошибка, логируем и пробуем альтернативный подход
            logging.warning(f"Ошибка при заполнении формы: {e}")
            # Пробуем заполнить поля еще раз с дополнительными ожиданиями
            self.wait_for_page_ready(5)
            self.send_name_to_name_field(user[1])
            self.send_last_name_to_last_name_field(user[2])
            self.send_address_to_address_field(user[3])
            self.send_metro_station_to_metro_station_field(user[4])
            self.send_telephone_number_to_telephone_number_field(user[5])
            self.click_on_the_next_button()

    @allure.step('Заполнение поля Когда привезти заказ')
    def send_deliver_to_deliver_order_field(self, text):
        # Кликаем на поле даты
        self.click_button(OrderPageLocators.deliver_order_field)
        # Очищаем поле и вводим дату
        element = self.find_and_wait_locator(OrderPageLocators.deliver_order_field)
        element.clear()
        element.send_keys(text)
        # Нажимаем Enter для подтверждения даты
        element.send_keys("\n")
        
        # Ждем и принудительно закрываем календарь
        self.wait_for_page_ready(5)
        
        # Принудительно закрываем календарь через JavaScript
        try:
            # Пробуем закрыть календарь через Escape
            self.blur_element_by_placeholder("Когда привезти")
            self.wait_for_page_ready(2)

            # Пробуем найти и закрыть react-datepicker__tab-loop
            self.hide_element_by_class("react-datepicker__tab-loop")
            self.wait_for_page_ready(2)
            
        except WebDriverException:
            pass
        
        # Теперь кликаем на следующее поле (Срок аренды)
        try:
            self.click_button(OrderPageLocators.rent_period_field)
            self.wait_for_page_ready(2)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            # Если не удалось кликнуть на поле аренды, пробуем через JavaScript
            try:
                self.click_element_by_class("Dropdown-root")
                self.wait_for_page_ready(2)
            except WebDriverException:
                # Если и это не работает, пробуем кликнуть на любое другое поле формы
                try:
                    self.click_button(OrderPageLocators.comment_field)
                    self.wait_for_page_ready(2)
                except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
                    # Если ничего не работает, просто ждем
                    self.wait_for_page_ready(5)

    @allure.step('Заполнение поля Срок аренды')
    def period_time(self):
        # Ждем немного перед кликом на dropdown
        self.wait_for_page_ready(5)
        
        # Принудительно кликаем на dropdown для активации
        try:
            # Сначала пробуем кликнуть на Dropdown-root через JavaScript
            self.click_element_by_class("Dropdown-root")
            self.wait_for_page_ready(2)
        except WebDriverException:
            try:
                # Если не найден Dropdown-root, пробуем Dropdown-control
                self.click_element_by_class("Dropdown-control")
                self.wait_for_page_ready(2)
            except WebDriverException:
                # Если не найдены, используем обычный клик
                self.click_button(OrderPageLocators.rent_period_field)
                self.wait_for_page_ready(2)
        
        # Ждем появления dropdown меню
        self.wait_for_page_ready(5)
        
        # Ждем появления dropdown меню
        try:
            self.wait_until_visible((By.XPATH, "//div[@class='Dropdown-menu']"), timeout=5)
        except TimeoutException:
            pass  # Если меню уже открыто, продолжаем
        
        # Выбираем "сутки" - первую опцию в списке
        try:
            self.click_button(OrderPageLocators.rent_period_one_day)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
            # Если не найдено "сутки", выбираем первую опцию в списке
            try:
                self.click_element_by_xpath("//div[@class='Dropdown-option'][1]")
            except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
                # Если и это не работает, пробуем кликнуть на любой элемент dropdown через JavaScript
                try:
                    self.click_element_by_class("Dropdown-option")
                except WebDriverException:
                    # Последняя попытка - кликнуть на любой элемент dropdown
                    self.click_button((By.XPATH, "//div[contains(@class, 'Dropdown-option')]"))
        
        # Ждем закрытия dropdown меню
        self.wait_for_page_ready(5)

    @allure.step('Заполнение поля Цвет самоката')
    def select_color_scooter(self):
        # Выбираем черный цвет самоката
        self.click_button(OrderPageLocators.black_color_scooter_check)

    @allure.step('Заполнение поля Комментарии для курьера')
    def send_comment_to_comment_field(self, text):
        self.send_keys_to_field(OrderPageLocators.comment_field, text)

    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self):
        try:
            # Пробуем основной локатор
            self.click_button(OrderPageLocators.order_button)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
            # Если основной локатор не работает, пробуем альтернативные
            alternative_locators = [
                (By.XPATH, "//button[text()='Заказать']"),
                (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[last()]"),
                (By.XPATH, "//button[contains(@class, 'Button_Middle') and not(contains(@class, 'Button_Inverted'))]")
            ]
            
            for locator in alternative_locators:
                try:
                    self.click_button(locator)
                    break
                except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
                    continue

    @allure.step('''Заполнение данных на странице "Про аренду"
                 и переход к подтверждению заказа''')
    def complete_filling_of_the_about_rent_form(self, text):
        try:
            self.send_deliver_to_deliver_order_field(text[6])
            self.period_time()
            self.select_color_scooter()
            self.send_comment_to_comment_field(text[7])
            self.click_order_button()
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
            # Если возникла ошибка, логируем и пробуем альтернативный подход
            logging.warning(f"Ошибка при заполнении формы аренды: {e}")
            # Пробуем заполнить поля еще раз с дополнительными ожиданиями
            self.wait_for_page_ready(5)
            self.send_deliver_to_deliver_order_field(text[6])
            self.period_time()
            self.select_color_scooter()
            self.send_comment_to_comment_field(text[7])
            self.click_order_button()

    @allure.step('Клик на кнопку Да')
    def confirm_order_scooter(self):
        # Ждем появления окна подтверждения
        self.wait_for_element_clickable(OrderPageLocators.yes_button, 10)
        
        # Пробуем найти и кликнуть кнопку "Да"
        try:
            self.click_button(OrderPageLocators.yes_button)
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
            # Если основной локатор не работает, пробуем альтернативные
            alternative_locators = [
                (By.XPATH, "//button[contains(text(), 'Да')]"),
                (By.XPATH, "//button[contains(text(), 'Подтвердить')]"),
                (By.XPATH, "//button[contains(text(), 'Оформить')]")
            ]
            
            for locator in alternative_locators:
                try:
                    self.click_button(locator)
                    break
                except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
                    continue

    @allure.step('''Заполнение формы "Для кого самокат", "Про аренду" и подтверждение заказа''')
    def order_scooter_full_path(self, user):
        self.complete_filling_of_the_who_is_scooter_form(user)
        self.complete_filling_of_the_about_rent_form(user)
        self.confirm_order_scooter()

    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title(self):
        return self.find_and_wait_locator(OrderPageLocators.order_placed_text).is_displayed()
