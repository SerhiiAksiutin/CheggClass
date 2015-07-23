"""
Problem 2 (optional)
Go to dice.com, search for qa job.
Click on any relult and print out the job description.
"""
from selenium import webdriver
import time
import unicodedata

# Running Chrome browser
browser = webdriver.Chrome()  # = webdriver.Firefox()

# Assigning URL
URL = 'http://www.dice.com/'

# Opening URL
browser.get(URL)

# Assigning a keyword
keyword = 'QA'

# Finding search field by ID
search_field = browser.find_element_by_id('search-field-keyword')
search_field.send_keys(keyword)

# Finding 'Find Tech Jobs' button by XPath and clicking on it
find_job_button = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/form/fieldset/div[4]/div/div[1]/button')
find_job_button.click()

# Making a pause for 'Sign Up For Job Alerts' pop up window
time.sleep(8)

# Verifying if pop up appears
check_pop_up = browser.find_element_by_id('myModalLabel')

pop_up_title = check_pop_up.text
print("The '%s' pop up appears" % (pop_up_title))

# Closing the pop up window once it appears
if pop_up_title == 'Sign Up For Job Alerts':
    close_button = browser.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/button').click()
    print('The pop up was closed')
else:
    raise Exception("Timeout while waiting the pop up. Please run the test again.")

# Printing the title of fifth position
title_fifth_elem = browser.find_element_by_xpath('//*[@id="position5"]').text
print("The title is '%s'" % (title_fifth_elem))

# Making a pause for ... ?
time.sleep(4)

# Selecting 5th element in search result page
fifth_elem = browser.find_element_by_xpath('//*[@id="position5"]').click()
# webdriver.ActionChains(browser).move_to_element(fifth_elem).click(fifth_elem).perform()

time.sleep(4)

discription = browser.find_element_by_xpath('//*[@id="jobdescSec"]/p[1]').text
print 'Job Description:"\n"', unicodedata.normalize('NFKD', discription).encode('ascii','ignore')

