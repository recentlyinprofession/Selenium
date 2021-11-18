from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
