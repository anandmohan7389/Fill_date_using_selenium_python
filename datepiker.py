from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
a = ActionChains(driver)
driver.get('https://www.makemytrip.com/')   
time.sleep(10)
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/label/p[1]').click()
time.sleep(3)

month_year = "May 2024"
year = month_year.split()
desired_year = year[1]
desired_month = year[0]

month_order = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

import pdb;pdb.set_trace()
years = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div').text
split_year = years.split()
months = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div').text.split()
if split_year[1] == desired_year:
    if months[0] == desired_month[0]:
        days = driver.find_elements(By.XPATH, '//*[@class="DayPicker-Day"]')
        for j in days:
            if j.get_attribute('aria-label') == ("Fri May 03 2024"):
                j.click()
                time.sleep(5)
    else:
        action_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]')
        action_button.click()

if desired_year > split_year[1]:
    while split_year[1] != desired_year:
        action_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]')
        action_button.click()
        var = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div').text.split()
        split_year[1] = var[1]
        time.sleep(2)
        if split_year[1] == desired_year:
            break       
    current_month = var[0]

    
    if month_order[desired_month] > month_order[current_month]:
        while desired_month != months[0]:
            action_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]')
            action_button.click()
            var = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div').text.split()
            months[0] = var[0]
            time.sleep(1)
            if desired_month == months[0]:
                days = driver.find_elements(By.XPATH, '//*[@class="DayPicker-Day"]')
                for j in days:
                    if j.get_attribute('aria-label') == ("Fri May 03 2024"):
                        j.click()
                        time.sleep(50)
                        break

    if month_order[desired_month] < month_order[current_month]:
        while desired_month != months[0]:
            action_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[1]')
            action_button.click()
            var = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div').text.split()
            months[0] = var[0]
            time.sleep(1)
            if desired_month == months[0]:
                days = driver.find_elements(By.XPATH, '//*[@class="DayPicker-Day"]')
                for j in days:
                    if j.get_attribute('aria-label') == ("Fri May 03 2024"):
                        j.click()
                        time.sleep(50)
                        break

    if desired_month == current_month:
        days = driver.find_elements(By.XPATH, '//*[@class="DayPicker-Day"]')
        for j in days:
            if j.get_attribute('aria-label') == ("Fri May 03 2024"):
                j.click()
                time.sleep(50)
                break