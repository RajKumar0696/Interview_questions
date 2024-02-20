import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.opencart.com/")
element = driver.find_element(By.CSS_SELECTOR,"div[id='cloud'] a[class='btn btn-primary btn-xl']")

# scroll by pixel
# driver.execute_script("window.scrollBy(0,1000);", "")

# scroll into view
driver.execute_script("arguments[0].scrollIntoView();", element)

# scroll end page
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# time.sleep(5)

# scroll return to starting page
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)