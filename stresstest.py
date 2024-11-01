import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def stress_test():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    wait = WebDriverWait(driver, 5)
    
    try:
    
        drag_and_drop_link = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Dragabble']")))
        drag_and_drop_link.click()
        time.sleep(1)
        
        driver.back()
        sortable_link = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Selectable']")))
        sortable_link.click()
        time.sleep(1)
    
    finally:
        driver.quit()

def gradual_load_test():
    for users in range(1, 5):  
        with ThreadPoolExecutor(max_workers=users) as executor:
            futures = [executor.submit(stress_test) for _ in range(users)]
            for future in futures:
                future.result()
        time.sleep(30)  

gradual_load_test()