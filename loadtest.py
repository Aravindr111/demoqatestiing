from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import time
def load_test():
   driver = webdriver.Chrome()
   driver.get("https://demoqa.com/")

# Using XPath to navigate
   try:
    # Locate and click on the Forms section
       start_time = time.time()
       forms_link = driver.find_element(By.XPATH, "//*[text()='Forms']")
       forms_link.click()
       forms_response_time = time.time() - start_time
       print(f"Forms response time: {forms_response_time} seconds")

       driver.back()
       start_time = time.time()
       widgets_link = driver.find_element(By.XPATH, "//*[text()='Widgets']")
       widgets_link.click()
       widgets_response_time = time.time() - start_time
       print(f"Widgets response time: {widgets_response_time} seconds")

   finally:
     driver.quit()

def simulate_load_test():
     with ThreadPoolExecutor(max_workers=1) as executor:

        futures = [executor.submit(load_test) for _ in range(1)]
        for future in futures:
            future.result() 

simulate_load_test()