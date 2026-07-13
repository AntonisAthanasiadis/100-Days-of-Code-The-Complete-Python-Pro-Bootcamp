from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.selenium.dev")

    downloads_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Downloads"))
    )

    downloads_link.click()

    wait.until(
        EC.title_contains("Downloads")
    )

    print(driver.title)
    print(driver.current_url)

finally:
    driver.quit()