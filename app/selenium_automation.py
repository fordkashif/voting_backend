from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

def automate_voting():
    # ChromeDriver setup (relative path to chromedriver)
    service = Service(executable_path="C:/Users/kjford/Documents/voting_automation_app/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    try:
        driver.delete_all_cookies()

        driver.get("https://sterlinggospelawards.com/vote-2024-peoples-choice/")
        
        first_button = driver.find_element(By.CSS_SELECTOR, "button[value='welcome']")
        first_button.click()

        time.sleep(3)

        checkbox_labels = ["Sara-Ann Edwards-Miller", "Alive - Sara-Ann Edwards-Miller - LOVE 101 F.M."]
        for label in checkbox_labels:
            checkbox = driver.find_element(By.XPATH, f"//div[@class='totalpoll-question-choices-item-label']/span[text()='{label}']")
            checkbox.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[value='vote']")
        submit_button.click()

        time.sleep(5)

    finally:
        driver.quit()
