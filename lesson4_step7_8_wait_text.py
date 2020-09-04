from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    book = browser.find_element_by_id('book')

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    
    book.click()

    submit = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

    x_el = browser.find_element_by_id('input_value')
    x = x_el.text

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    submit.click()

finally:
    time.sleep(10)
    browser.quit()
