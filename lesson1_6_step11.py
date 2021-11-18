from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(executable_path='C:/users/anast/downloads/chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("testFirstName")
    input2 = browser.find_element_by_tag_name(".first_block .form-group.second_class input")
    input2.send_keys("testLastName")
    input3 = browser.find_element_by_xpath("//div[@class=\"first_block\"]//input[@class=\"form-control third\"]")
    input3.send_keys("testEmail")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()