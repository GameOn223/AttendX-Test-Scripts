from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")
driver.find_element(By.ID, "username").send_keys("teacher1")
driver.find_element(By.ID, "password").send_keys("pass123")
driver.find_element(By.ID, "login-btn").click()

driver.get("http://localhost:3000/attendance")
driver.find_element(By.ID, "student-1-present").click()
driver.find_element(By.ID, "save-btn").click()

msg = driver.find_element(By.ID, "message").text
if "saved" in msg.lower():
    print("PASS")
else:
    print("FAIL")

driver.quit()
