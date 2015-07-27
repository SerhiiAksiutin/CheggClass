# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1. Write a function called element_exists
that will check if an element exists on the page and returns a True or False.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Running browser >
driver = webdriver.Firefox()

# Maximizing the browser >
driver.maximize_window()

# Assigning the URL >
url = 'http://www.chegg.com/schools'

# Opening the URL
driver.get(url)

# Assigning the keyword >
keyword = 'Stanford University'

# Finding the search field >
search_field = driver.find_element_by_id('schools-search-input')

# Sending the keyword
search_field.send_keys(keyword)
search_field.send_keys(Keys.RETURN)


# Waiting the result
wait = WebDriverWait(driver, 30)
search_result = wait.until(
  EC.element_to_be_clickable((By.LINK_TEXT, 'Stanford University'))).click()

# Checking the element >


def element_exists():
    try:
        find_menu_emem = wait.until(
          EC.presence_of_element_located((By.LINK_TEXT, 'Student Rankings')))
        if find_menu_emem.text == 'Student Rankings':
            print('Congratulation! The element "%s" exists.' % (
              find_menu_emem.text))
            return True
    except:
        print("Sorry! This element doesn't exist.")
        return False
print element_exists()
