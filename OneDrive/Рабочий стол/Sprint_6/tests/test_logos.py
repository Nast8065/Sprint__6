import allure
from pages.main_page import HeaderPage, MainPage
from pages.order_page import OrderPage
from helpers.data import Users


class TestLogos:

#Тестовый класс для функциональности логотипов

    @allure.title('Проверка перенаправления по логотипу Самоката с главной страницы')
    @allure.description('Проверяем, что клик по логотипу Самоката перенаправляет на главную страницу')
    def test_scooter_logo_redirect_from_main_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookies()
        initial_url = main_page.get_current_url()
        header_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert current_url == initial_url, f"URL сменился после клика по логотипу Самоката: {current_url}"

    @allure.title('Проверка перенаправления по логотипу Яндекса')
    @allure.description('Проверяем, что клик по логотипу Яндекс открывает новую вкладку дзен')
    def test_yandex_logo_redirect(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookies()
        initial_windows_count = main_page.get_windows_count()
        header_page.click_yandex_logo()
        main_page.wait_for_new_window(initial_windows_count)
        # Проверяем, что открылась новая вкладка
        new_windows_count = main_page.get_windows_count()
        assert new_windows_count > initial_windows_count, "Новая вкладка не открылась"
        header_page.go_to_new_tab()
        main_page.wait_for_page_ready(10)
        main_page.wait_for_url_change_from_about_blank(10)
        # Проверяем URL новой вкладки
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex.ru" in current_url, \
            f"Новая вкладка не содержит ожидаемый URL: {current_url}"
        # Проверяем заголовок страницы
        main_page.wait_for_page_title_loaded()
        page_title = main_page.get_page_title()
        assert "дзен" in page_title or "Яндекс" in page_title or "Yandex" in page_title, \
            f"Заголовок страницы не содержит ожидаемый текст: {page_title}"

    @allure.title('Проверка перенаправления по логотипу Самоката со страницы заказа')
    @allure.description('Проверяем, что клик по логотипу Самоката со страницы заказа отправляет на главную страницу')
    def test_scooter_logo_redirect_from_order_page(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookies()
        main_page.scroll_and_click_order_button()
        order_page.complete_filling_of_the_who_is_scooter_form(Users.user1)
        # Кликаем по логотипу Самоката со страницы заказа
        header_page.click_scooter_logo()
        # Проверяем, что вернулись на главную страницу
        current_url = main_page.get_current_url()
        assert "order" not in current_url, f"Не вернулись на главную страницу: {current_url}"

    @allure.title('Проверка атрибутов логотипов')
    @allure.description('Проверяем корректность атрибутов логотипов')
    def test_logos_attributes(self, driver):
        header_page = HeaderPage(driver)
        main_page = MainPage(driver)
        main_page.accept_cookies()
        # Проверяем, что логотипы являются ссылками
        assert header_page.is_logo_link('scooter'), "Логотип Самоката не является ссылкой"
        assert header_page.is_logo_link('yandex'), "Логотип Яндекса не является ссылкой"
        # Проверяем target="_blank" для логотипа Яндекса
        yandex_target = header_page.get_logo_target('yandex')
        assert yandex_target == '_blank', f"Логотип Яндекса не имеет target='_blank': {yandex_target}"
        # Проверяем href атрибуты
        scooter_href = header_page.get_logo_href('scooter')
        yandex_href = header_page.get_logo_href('yandex')
        
        assert scooter_href is not None, "Логотип Самоката не имеет href атрибута"
        assert yandex_href is not None, "Логотип Яндекса не имеет href атрибута"
