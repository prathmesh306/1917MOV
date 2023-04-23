from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print("sample test case started")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("C:/Users/dell/Desktop/selinium/form.html")
time.sleep(3)

driver.find_element(By.NAME, 'name').send_keys("PRATHMESH PATEL")
time.sleep(3)

driver.find_element(By.NAME, 'email').send_keys("prathmeshpatel306@gmail.com")
time.sleep(3)

driver.find_element(By.NAME, 'message').send_keys("implemented by prathmeshpatel , Exp No. 6. ")
time.sleep(3)

driver.find_element(By.NAME, "button").send_keys(Keys.ENTER)
time.sleep(3)

driver.close()
print("sample test case successfully completed")