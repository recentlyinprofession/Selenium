from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.implicitly_wait(5)
    browser.get(link)

    WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_tag_name("button")
    button.click()

    x = browser.find_element_by_css_selector("#input_value").text

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
