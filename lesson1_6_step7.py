from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("[class=\"first_block\"] input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
