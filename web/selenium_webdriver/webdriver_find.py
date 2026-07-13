from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
print("Navigating to the \"Selenium\" Wikipedia page!")
try:
    driver.get("https://www.wikipedia.org")

    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    print(driver.current_url)

finally:
    driver.quit()