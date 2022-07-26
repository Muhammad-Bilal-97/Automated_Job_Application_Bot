from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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


time.sleep(5)

all_listings = driver.find_element(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # try to locate apply button, if can't locate then skip the jobs.
    try:
        apply_button = driver.find_element(By.CLASS_NAME, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # if application requires phone number and the field is empty, then fill in the number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        # submit the application
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # if the submit button is a "Next" button, then this is a multi-step applicaiton so skip.
        if submit_button.get_attribute("data-control-name") == "contine_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)

            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
