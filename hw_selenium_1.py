"""
Problem 2 (optional)
Go to dice.com, search for qa job.
Click on any relult and print out the job description.
"""
from selenium import webdriver
import time
import unicodedata

# Running Chrome browser
# browser = webdriver.Chrome()
browser = webdriver.Firefox()
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

# Making a pause for 'Sign Up For Job Alerts' pop up window... \Implicit Waits needs to be implemented
time.sleep(8)

# Verifying if pop up appears
try:
    check_pop_up = browser.find_element_by_id('myModalLabel')
    pop_up_title = check_pop_up.text
    print("The '%s' pop up appears" % (pop_up_title))

    # Closing the pop up window once it appears
    if pop_up_title == 'Sign Up For Job Alerts':
        close_button = browser.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/button').click()
        print('The pop up was closed')
    else:
        raise Exception("Timeout while waiting the pop up. Please run the test again.")
except:
    pass

# Printing the title of fifth position
fifth_elem = browser.find_element_by_xpath('//*[@id="position5"]')
title_text = fifth_elem.text
print("The title is '%s'" % (title_text))

# Making a pause for ... Implicit Waits needs to be implemented
time.sleep(4)

# Selecting 5th element in search result page
fifth_elem.click()

# Making a pause for ... Implicit Waits needs to be implemented
time.sleep(4)

#  Printing the description of the job
# description = browser.find_element_by_id('jobdescSec') #  should work whit PyCharm
# print description.text #  should work whit PyCharm
description = browser.find_element_by_xpath('//*[@id="jobdescSec"]/p[1]').text
print 'Job Description:"\n"', unicodedata.normalize('NFKD', description).encode('ascii', 'ignore')
