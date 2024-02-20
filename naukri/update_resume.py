import time

from selenium_py import webdriver
from selenium_py.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[@id='login_Layer']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys("mrajkumar0696@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").clear()
driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Muruga@3")
driver.find_element(By.XPATH, "//button[@class='btn-primary loginButton']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='View profile']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='card mt15']//div//span[@class='edit icon'][normalize-space()="
                              "'editOneTheme']").click()
time.sleep(5)
# driver.find_element((By.CLASS_NAME, "btn-dark-ot")).click()
driver.save_screenshot("naukri.png")

time.sleep(5)
driver.close()