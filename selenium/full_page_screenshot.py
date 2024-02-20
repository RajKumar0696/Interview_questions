from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.EdgeOptions()
options.add_argument("--headless")
driver = webdriver.Edge(options=options)  # It will work only headless mode
driver.get("https://www.geeksforgeeks.org/with-statement-in-python/")
width = 1336  # open display settings--> display resolutions--> first value is width of computer
height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
                               "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
                               "document.documentElement.offsetHeight);")
driver.set_window_size(width, height)
full_page = driver.find_element(By.TAG_NAME, "body")
full_page.screenshot(r"C:\Users\WELCOME\Desktop\Interview_quations\selenium\full_page.png")
driver.close()
