from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path=r"C:\Users\WELCOME\Downloads\chromedriver-win64\chromedriver-win64"
                                          r"\chromedriver.exe")
driver.get("https://www.flipkart.com/")
driver.find_element(By.XPATH, "//input[@name='q']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text()='mobiles']").click()
time.sleep(5)
driver.close()
