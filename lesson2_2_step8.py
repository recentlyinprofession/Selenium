from selenium import webdriver
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("test")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("test")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test")

    fileButton = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'answer.txt')
    fileButton.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

file_path = os.path.join(current_dir, 'output.txt')
