from selenium.webdriver.common.by import By


class HeaderLocators:
    """
    Элементы навигации в хедере страницы
    """
    yandex_logo = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    scooter_logo = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    order_button = (By.XPATH, "//button[text()='Заказать'][1]")
    order_status_button = (By.XPATH, "//button[text()='Статус заказа']")
    order_number_input = (By.XPATH, "//input[@class='Input_Input__1iN_Z Header_Input__xIoUq']")
    go_button = (By.XPATH, "//button[text()='Go!']")
    header_title = (By.XPATH, "//div[text()='Учебный тренажер']")


class MainPageLocators:
    """
    Элементы главной страницы
    """
    order_button = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']")
    cookie_accept_button = (By.XPATH, "//button[@id='rcc-confirm-button']")
    faq_section_title = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Кнопки вопросов FAQ
    faq_questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    # Элементы с текстом ответов FAQ
    faq_answers = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]
