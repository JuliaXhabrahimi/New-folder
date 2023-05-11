#!/usr/bin/env python
# coding: utf-8

# In[22]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()  

# Navigate to the registration page
driver.get("https://www.teachaway.com")


# Click the Register button to open the registration form
driver.find_element(By.XPATH, '//*[@id="register"]').click()



   

# Wait for the registration form to load
wait = WebDriverWait(driver, 30)
wait.until(EC.visibility_of_element_located((By.ID, 'first_name')))



# Fill in the registration form.
driver.find_element(By.ID, 'first_name').send_keys("Jusltgi")
driver.find_element(By.ID, 'last_name').send_keys("Peaew")
driver.find_element(By.ID, 'email').send_keys("nadra@example.com")
driver.find_element(By.ID, 'password').send_keys("SecurePassword123")



# Submit the registration form.
driver.find_element(By.ID, 'create_account_action').click()

# Wait for the registration to complete.
wait.until(EC.visibility_of_element_located((By.ID, 'welcome-firstName')))

# First, click the dropdown menu to open it. Replace 'dropdown_menu' with the actual ID or XPATH.
dropdown_menu = driver.find_element(By.ID, 'hs-eu-decline-button')
dropdown_menu.click()

wait = WebDriverWait(driver, 10)

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div[1]/div[1]/div[2]/button')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="welcome-job-category"]/div/ul/li[1]')))
option.click()


# Then, click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="esl"]/div[2]/div[2]')
option.click()

# Then, click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="teaching-license"]/div[2]/div[2]')
option.click()

# After filling out the form, click the 'Submit' or 'Next' button
driver.find_element(By.ID, 'get-started').click()

# Wait for the next page to load and verify that the form submission was successful.
# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.ID, 'interests')))

wait = WebDriverWait(driver, 10)

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="schoolContactDirectly"]/div[2]/div[1]')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="interesedOnlineTeaching"]/div[2]/div[1]')))
option.click()

# Wait for the second option to be visible and then click it
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="interesedTEFL"]/div[2]/div[1]')))
option.click()

# Wait for the third option to be visible and then click it
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="interesedTeacherCertification"]/div[2]/div[1]')))
option.click()


# After filling out the form, click the 'Submit' or 'Next' button
driver.find_element(By.ID, 'next-to-about').click()

# Wait for the next page to load and verify that the form submission was successful.
# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.ID, 'country-tooltip-toggle')))

wait = WebDriverWait(driver, 10)

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[1]/div[2]/input')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/ul/li[4]')))
option.click()

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[2]/div[2]/button')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="state"]/div/ul/li[1]')))
option.click()

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[3]/div/div[2]/input')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/form/div[3]/div/div[2]/div[3]/div/ul/li[1]')))
option.click()

# Click on an empty area of the page after clicking the desired element
empty_area = driver.find_element(By.XPATH, '//body')
ActionChains(driver).click(empty_area).perform()




# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[4]/div/div[2]/input')))
dropdown_menu.click()

# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/form/div[4]/div/div[2]/div[3]/div/ul/li[1]')))
option.click()

# Click on an empty area of the page after clicking the desired element
empty_area = driver.find_element(By.XPATH, '//body')
ActionChains(driver).click(empty_area).perform()



# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[1]/div/button')))
dropdown_menu.click()
# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="monthOfBirth"]/div/ul/li[1]')))
option.click()

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div/button')))
dropdown_menu.click()
# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="dayOfBirth"]/div/ul/li[1]')))
option.click()

# Wait until the dropdown menu appears, then click it
dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[3]/div/button')))
dropdown_menu.click()
# Then, click the option you want
option = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yearOfBirth"]/div/ul/li[20]')))
option.click()

# Click the dropdown menu to open it.
dropdown_menu = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[1]/div/button')
dropdown_menu.click()

# Click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="country code"]/div/ul/li[7]')
option.click()


# Enter the phone number in the input field.
phone_field = wait.until(EC.visibility_of_element_located((By.ID, 'phoneNumber')))
phone_field.send_keys("68 312 2345")

# After filling out the form, click the 'Submit' or 'Next' button
next_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="next-step"]')))
next_button.click()

# Wait for the next page to load and verify that the form submission was successful.
# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/form/div[1]/div[1]/h4')))

# Click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="noEducation"]')
option.click() 

# After filling out the form, click the 'Submit' or 'Next' button
driver.find_element(By.ID, 'next-step').click()

# Wait for the next page to load and verify that the form submission was successful.
# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/form/div[2]/div[1]/h4')))

# Click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="checkbox-no-experience"]')
option.click() 

# After filling out the form, click the 'Submit' or 'Next' button
driver.find_element(By.ID, 'complete-next').click()

# Wait for the next page to load and verify that the form submission was successful.
# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.ID, 'apply-for-jobs-desktop')))

# Click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[5]')
option.click()  


# Click the option you want. Replace 'option_xpath' with the actual XPATH.
option = driver.find_element(By.XPATH, '//*[@id="menu"]/ul/li[4]')
option.click()  

# This could involve waiting for a specific element to become visible, or checking the page's URL.
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div[2]/div/button[1]')))

# Fill in the registration form.
driver.find_element(By.ID, 'username').send_keys("nadra@example.com")
driver.find_element(By.ID, 'password').send_keys("SecurePassword123")

# Submit the registration form.
driver.find_element(By.ID, 'login_action').click()

# Wait for the registration to complete.
wait.until(EC.visibility_of_element_located((By.ID, 'complete-profile-cta')))

time.sleep(10)
driver.quit()


# In[ ]:




