from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.nationalcar.com/en/home.html")
elem = driver.find_element_by_id("search-autocomplete__input-PICKUP")
elem.clear()
try:
    elem.send_keys("Atlanta Hartsfield-Jackson Intl.")
    driver.implicitly_wait(10)  # seconds
    # EC.presence_of_element_located((By.CLASS_NAME, "input-pseudo__input"))
    print(str(driver.page_source()))
    elem.send_keys(Keys.RETURN)
    but = driver.find_element_by_id("date-time__pickup-toggle")

    print(elem.get_attribute('innerHTML'))
    but.click()

finally:
    driver.quit()




