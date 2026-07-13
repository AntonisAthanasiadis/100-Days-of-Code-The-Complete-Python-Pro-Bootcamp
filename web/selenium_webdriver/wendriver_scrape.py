from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    driver.get("https://en.wikipedia.org/wiki/Selenium")

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "firstHeading"))
    )

    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")

    print("Title:", heading.text)
    print()

    for p in paragraphs[:5]:
        text = p.text.strip()
        if text:
            print(text)
            print()

finally:
    driver.quit()