import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(r"C:\Users\WELCOME\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe",
                          options=options)
driver.get("https://www.browserstack.com/guide/headless-browser-testing-selenium-python")
driver.find_element(By.XPATH, "//div[@class='guide-tags__badge guide-tags__article-section--newsletter']"
                              "//a[@title='Selenium']").click()
time.sleep(5)
driver.close()
