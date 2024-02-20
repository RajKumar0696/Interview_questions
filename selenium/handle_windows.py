from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\WELCOME\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver.get("")
win_id = driver.current_window_handle
win_ids = driver.window_handles
driver.switch_to.window(win_id)

