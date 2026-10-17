from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")
driver.find_element(By.ID, "username").send_keys("teacher1")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "login-btn").click()

if "dashboard" in driver.current_url:
    print("FAIL")
else:
    print("PASS")

driver.quit()
