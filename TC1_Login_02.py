from selenium import webdriver
from selenium.webdriver.common.by import By
driver_1 = webdriver.Chrome()
driver_1.maximize_window()
driver_1.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver_1.implicitly_wait(20)
driver_1.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver_1.find_element(By.XPATH, "//*[@type='password']").send_keys("Invalid Password")
driver_1.find_element(By.XPATH, "//*[@type='submit']").click()
driver_1.implicitly_wait(20)
print("Invalid credentials")
