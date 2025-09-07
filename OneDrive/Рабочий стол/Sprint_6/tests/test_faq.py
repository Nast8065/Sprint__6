import allure
import pytest
from helpers.data import FAQAnswers
from pages.main_page import MainPage


class TestFAQ:

#Тестовый класс для функциональности FAQ

    @allure.title('Проверка отображения раздела FAQ')
    @allure.description('Проверяем, что раздел "Вопросы о важном" отображается на странице')
    def test_faq_section_visible(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        assert main_page.is_faq_section_visible(), "Раздел FAQ не отображается"
        
    @allure.title('Проверка количества вопросов FAQ')
    @allure.description('Проверяем, что все 8 вопросов FAQ отображаются на странице')
    def test_faq_questions_count(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        questions_count = main_page.get_faq_questions_count()
        assert questions_count == 8, f"Должно быть 8 вопросов, фактически: {questions_count}"

    @pytest.mark.parametrize("question_index,expected_answer",[(i, FAQAnswers.expected_answers[i]) for i in range(8)],ids=[f"question_{i}" for i in range(8)])
    @allure.title('Проверка наличия ответов на вопросы FAQ')
    @allure.description('Проверяем, что при нажатии на вопрос, отображается правильный ответ')
    def test_faq_answers(self, driver, question_index, expected_answer):

#Тест проверяет, что при нажатии на любой вопрос FAQ, отображается верный ответ

        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        # Получаем текст ответа
        actual_answer = main_page.get_faq_answer_text(question_index)
        
        # Проверяем соответствие ожидаемого и фактического ответа
        assert actual_answer == expected_answer, \
            f"Ответ по плану: '{expected_answer}', Фактический ответ: '{actual_answer}'"
