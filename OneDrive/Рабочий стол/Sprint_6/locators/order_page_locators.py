from selenium.webdriver.common.by import By


class OrderPageLocators:
    """
    Локаторы для формы заказа самоката
    """
    # Поля первой страницы формы заказа
    name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro = (By.XPATH, ".//div[text() = 'Тверская']")
    telephone_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Далее']")

    # Поля второй страницы формы заказа
    deliver_order_field = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_period_field = (By.XPATH, "//div[@class='Dropdown-placeholder']")
    rent_period_one_day = (By.XPATH, "//div[@class='Dropdown-option' and contains(text(), 'сутки')]")
    black_color_scooter_check = (By.ID, 'black')
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

    # Кнопки окна подтверждения заказа
    no_button = (By.XPATH, "//button[text()='Нет']")
    yes_button = (By.XPATH, "//button[text()='Да']")

    # Текст успешного оформления заказа
    order_placed_text = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")