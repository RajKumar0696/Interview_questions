from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://www.google.com/")
# xpath = "//input[@name='search']"
# css = "input.form-control form-control-lg"
# driver.find_element(By.CSS_SELECTOR, css).send_keys("123456")
# time.sleep(8)
# sug = driver.find_elements(By.CSS_SELECTOR,"#APjFqb")
suggestion_element = driver.find_element(By.XPATH,"//ul[@class='suggestion-list']/li[@class='suggestion']")

for su in suggestion_element:
    print(su.text)