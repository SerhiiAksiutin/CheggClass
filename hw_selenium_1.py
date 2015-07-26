"""
Problem 2 (optional)
Go to dice.com, search for QA job.
Click on any result and print out the job description.
"""
from selenium import webdriver
# import time
import unicodedata
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# Running Chrome browser >
browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# Maximizing browser window >
browser.maximize_window()
# Assigning URL >
URL = 'http://www.dice.com/'

# Opening URL >
browser.get(URL)

# Assigning a keyword >
keyword = 'QA'

# Finding search field by ID >
search_field = browser.find_element_by_id('search-field-keyword')
search_field.send_keys(keyword)

# Finding 'Find Tech Jobs' button by XPath and clicking on it >
find_job_button = browser.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/form/fieldset/div[4]/div/div[1]/button')
find_job_button.click()


wait = WebDriverWait(browser, 30)

# Verifying and waiting if pop up appears >
try:
    check_pop_up = browser.find_element_by_id('myModalLabel')
    pop_up_title = check_pop_up.text
    print("The '%s' pop up appears" % (pop_up_title))

# Closing the pop up window once it appears >
    if pop_up_title == 'Sign Up For Job Alerts':
        skip_pop_up = wait.until(
            EC.presence_of_element_located((By.ID, 'myModalLabel')))

        print('The pop up "%s" was closed' % (pop_up_title))
        skip_pop_up.click()
    else:
        raise Exception(
            "Timeout while waiting the pop up. Please run the test again.")
except:
    pass

# fifth_elem = browser.find_element_by_id('position0')
print('PASS=============================================================')

# Printing the title of fifth position >
# fifth_elem = wait.until(
#     EC.visibility_of_element_located((By.ID, 'position0')))
# fifth_elem = wait.until(EC.element_to_be_clickable((By.ID, 'position0')))
fifth_elem = wait.until(EC.presence_of_element_located((By.ID, 'position0')))
# ActionChains(browser).move_to_element(fifth_elem).perform()
title_text = fifth_elem.text
print("The title is '%s'" % (title_text))

# Selecting 5th element in search result page >
fifth_elem.click()
print('PASS=============================================================')

# Making a pause for ... Implicit Waits needs to be implemented >
wait_description = wait.until(
    EC.presence_of_element_located((By.ID, 'position0')))

# Printing the description of the job >
description = browser.find_element_by_id('jobdescSec').text
print 'Job Description:\n', unicodedata.normalize(
    'NFKD', description).encode('ascii', 'ignore')
