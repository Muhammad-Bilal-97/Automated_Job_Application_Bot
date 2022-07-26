from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
ACCOUNT_PASSWORD = "YOUR_LOGIN_PASSWORD"
PHONE = "YOUR PHONE NUMBER"

chrome_driver_path = "D:\Development\chromedriver_v103\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_WT=1%2C2%2C3&geoId=101022442&keywords=python&location=Pakistan")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
# email field
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
# password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# locate to apply button
time.sleep(5)
apply_button = driver.find_element(By.CLASS_NAME, ".jobs-s-apply button")
apply_button.click()

# if application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

# submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
