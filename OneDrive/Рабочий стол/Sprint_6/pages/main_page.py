import allure
from locators.homepage_locators import HeaderLocators, MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
#Page Object для элементов навигации в хедере

    @allure.step('Клик по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_button(HeaderLocators.yandex_logo)

    @allure.step('Клик по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_button(HeaderLocators.scooter_logo)

    @allure.step('Клик по кнопке Заказать в хедере')
    def click_order_button(self):
        self.click_button(HeaderLocators.order_button)

    @allure.step('Клик по кнопке Статус заказа')
    def click_order_status_button(self):
        self.click_button(HeaderLocators.order_status_button)

    @allure.step('Заполнение номера заказа')
    def enter_order_number(self, number):
        self.send_keys_to_field(HeaderLocators.order_number_input, number)

    @allure.step('Клик по кнопке Go!')
    def click_go_button(self):
        self.click_button(HeaderLocators.go_button)

    @allure.step('Проверка статуса заказа')
    def check_order_status(self, number):
        self.click_order_status_button()
        self.enter_order_number(number)
        self.click_go_button()

    @allure.step('Проверка отображения заголовка страницы')
    def check_page_title(self):
        return self.check_element(HeaderLocators.header_title)

    @allure.step('Проверка атрибутов логотипа Самоката')
    def get_scooter_logo_attributes(self):
        #Получение атрибутов логотипа Самоката

        scooter_logo = self.find_and_wait_locator(HeaderLocators.scooter_logo)
        return {
            'tag_name': scooter_logo.tag_name,
            'href': scooter_logo.get_attribute('href'),
            'target': scooter_logo.get_attribute('target')
        }

    @allure.step('Проверка атрибутов логотипа Яндекса')
    def get_yandex_logo_attributes(self):
        #Получение атрибутов логотипа Яндекса
        yandex_logo = self.find_and_wait_locator(HeaderLocators.yandex_logo)
        return {
            'tag_name': yandex_logo.tag_name,
            'href': yandex_logo.get_attribute('href'),
            'target': yandex_logo.get_attribute('target')
        }

    @allure.step('Проверка что логотип является ссылкой')
    def is_logo_link(self, logo_type):
        #Проверка что логотип является ссылкой
        if logo_type == 'scooter':
            attributes = self.get_scooter_logo_attributes()
        elif logo_type == 'yandex':
            attributes = self.get_yandex_logo_attributes()
        else:
            raise ValueError(f"Неизвестный тип логотипа: {logo_type}")
        
        return attributes['tag_name'] == 'a'

    @allure.step('Проверка target атрибута логотипа')
    def get_logo_target(self, logo_type):
        #Получение target атрибута логотипа
        if logo_type == 'scooter':
            attributes = self.get_scooter_logo_attributes()
        elif logo_type == 'yandex':
            attributes = self.get_yandex_logo_attributes()
        else:
            raise ValueError(f"Неизвестный тип логотипа: {logo_type}")
        
        return attributes['target']

    @allure.step('Проверка href атрибута логотипа')
    def get_logo_href(self, logo_type):
        #Получение href атрибута логотипа
        if logo_type == 'scooter':
            attributes = self.get_scooter_logo_attributes()
        elif logo_type == 'yandex':
            attributes = self.get_yandex_logo_attributes()
        else:
            raise ValueError(f"Неизвестный тип логотипа: {logo_type}")
        
        return attributes['href']


class MainPage(BasePage):
    #Page Object для элементов главной страницы

    @allure.step('Принятие cookies')
    def accept_cookies(self):
        self.click_button(MainPageLocators.cookie_accept_button)

    @allure.step('Скролл и клик по кнопке Заказать на главной странице')
    def scroll_and_click_order_button(self):
        self.scroll_to_locator(MainPageLocators.order_button)
        self.click_button(MainPageLocators.order_button)

    @allure.step('Переход к разделу вопросов')
    def scroll_to_faq_section(self):
        self.scroll_to_locator(MainPageLocators.faq_section_title)

    @allure.step('Клик по вопросу FAQ')
    def click_faq_question(self, question_index):
        self.scroll_to_faq_section()
        self.click_button(MainPageLocators.faq_questions[question_index])

    @allure.step('Получение текста ответа FAQ')
    def get_faq_answer_text(self, question_index):
        self.click_faq_question(question_index)
        return self.get_text_locator(MainPageLocators.faq_answers[question_index])

    @allure.step('Проверка количества вопросов FAQ')
    def get_faq_questions_count(self):
        return len(MainPageLocators.faq_questions)

    @allure.step('Проверка видимости раздела FAQ')
    def is_faq_section_visible(self):
        return self.check_element(MainPageLocators.faq_section_title)
