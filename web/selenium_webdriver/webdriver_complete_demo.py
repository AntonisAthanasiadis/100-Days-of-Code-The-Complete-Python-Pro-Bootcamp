import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    #Text input
    driver.find_element(By.NAME, "my-text").send_keys("Antonios")
    time.sleep(2)

    #Password
    driver.find_element(By.NAME, "my-password").send_keys("secret123")
    time.sleep(2)

    #Text area
    driver.find_element(By.NAME, "my-textarea").send_keys(
        "Testing Selenium forms."
    )
    time.sleep(2)

    #Dropdown
    dropdown = Select(
        driver.find_element(By.NAME, "my-select")
    )
    dropdown.select_by_visible_text("Two")
    time.sleep(2)

    #Checkbox
    checkbox = driver.find_element(By.ID, "my-check-1")
    if not checkbox.is_selected():
        checkbox.click()
    time.sleep(2)
    #Radio button
    driver.find_element(By.ID, "my-radio-2").click()
    time.sleep(2)
    #Submit
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button")
        )
    ).click()

    #Wait for confirmation page
    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    print("Result:", message.text)
    time.sleep(2)
finally:
    driver.quit()
