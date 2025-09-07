from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException


class BasePage:
    """
    Базовый класс для всех страниц с общими методами
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_until_visible(self, locator, timeout=10):
        """
        Ожидание видимости элемента
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_present(self, locator, timeout=10):
        """
        Ожидание присутствия элемента в DOM
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def get_current_url(self):
        """
        Получение текущего URL страницы
        """
        return self.driver.current_url

    def find_and_wait_locator(self, locator):
        """
        Поиск и ожидание элемента
        """
        return self.wait_until_visible(locator, timeout=10)

    def click_button(self, locator):
        """
        Клик по элементу с fallback на JavaScript
        """
        element = self.find_and_wait_locator(locator)
        try:
            element.click()
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
            # Если обычный клик не работает, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys_to_field(self, locator, text):
        """
        Ввод текста в поле с предварительной очисткой
        """
        element = self.find_and_wait_locator(locator)
        # Очищаем поле перед вводом
        element.clear()
        # Вводим текст
        element.send_keys(text)

    def get_text_locator(self, locator):
        """
        Получение текста элемента
        """
        return self.find_and_wait_locator(locator).text

    def scroll_to_locator(self, locator):
        """
        Скролл к элементу с центрированием
        """
        element = self.find_and_wait_locator(locator)
        # Скролл с отступом, чтобы элемент был виден и не перекрывался
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        # Дополнительный скролл вверх для избежания перекрытия изображением
        self.driver.execute_script("window.scrollBy(0, -100);")
        # Ждем завершения анимации скролла
        WebDriverWait(self.driver, 2).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def go_to_new_tab(self):
        """
        Переключение на новую вкладку
        """
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        """
        Проверка отображения элемента
        """
        return self.find_and_wait_locator(locator).is_displayed()

    def wait_for_page_ready(self, timeout=5):
        """
        Ожидание готовности страницы
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_for_element_clickable(self, locator, timeout=5):
        """
        Ожидание кликабельности элемента
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def execute_js_script(self, script):
        """
        Выполнение JavaScript скрипта
        """
        return self.driver.execute_script(script)

    def blur_element_by_placeholder(self, placeholder_text):
        """
        Убираем фокус с элемента по placeholder
        """
        script = f'document.querySelector("input[placeholder*=\\"{placeholder_text}\\"]").blur();'
        self.execute_js_script(script)

    def hide_element_by_class(self, class_name):
        """
        Скрытие элемента по классу
        """
        script = f"""
            var element = document.querySelector('.{class_name}');
            if (element) {{
                element.style.display = 'none';
            }}
        """
        self.execute_js_script(script)

    def click_element_by_class(self, class_name):
        """
        Клик по элементу по классу
        """
        script = f'document.querySelector(".{class_name}").click();'
        self.execute_js_script(script)

    def click_element_by_xpath(self, xpath):
        """
        Клик по элементу по XPath
        """
        element = self.driver.find_element("xpath", xpath)
        element.click()

    def wait_for_new_window(self, initial_windows_count, timeout=10):
        """
        Ожидание открытия новой вкладки
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > initial_windows_count
        )

    def wait_for_page_title_loaded(self, timeout=10):
        """
        Ожидание загрузки заголовка страницы
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.title and len(d.title.strip()) > 0
        )

    def get_page_title(self):
        """
        Получение заголовка страницы
        """
        return self.driver.title

    def get_windows_count(self):
        """
        Получение количества открытых окон
        """
        return len(self.driver.window_handles)

    def wait_for_url_change_from_about_blank(self, timeout=10):
        """
        Ожидание изменения URL с about:blank
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != "about:blank" and "about:" not in d.current_url
        )
