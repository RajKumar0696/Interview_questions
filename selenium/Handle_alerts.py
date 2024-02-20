from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\WELCOME\Downloads\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver.get("")
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
value = alert.text
