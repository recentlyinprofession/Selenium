from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.get(link)

    x = browser.find_element_by_css_selector("#input_value").text

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
