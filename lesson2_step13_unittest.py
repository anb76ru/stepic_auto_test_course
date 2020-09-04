import unittest
from selenium import webdriver
import time

def reg_1():
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('.first_block .first_class input')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('.first_block .second_class input')
    last_name.send_keys('Petrov')
    user_mail = browser.find_element_by_css_selector('.first_block .third_class input')
    user_mail.send_keys('1@ya.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text
    
def reg_2():
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector('.first_block .first_class input')
    first_name.send_keys('Ivan')
    last_name = browser.find_element_by_css_selector('.first_block .second_class input')
    last_name.send_keys('Petrov')
    user_mail = browser.find_element_by_css_selector('.first_block .third_class input')
    user_mail.send_keys('1@ya.ru')
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text
    

registration_message = "Congratulations! You have successfully registered!"

class TestReg(unittest.TestCase):
    def test_reg_1(self): 
        self.assertEqual(reg_1(), registration_message, 'Test FAILED')

    def test_reg_2(self):
        self.assertEqual(reg_2(), registration_message, 'Test FAILED')

if __name__ == "__main__":
    unittest.main()