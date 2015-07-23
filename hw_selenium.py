# Problem 1
# 1. Go to ebay and search 261972139580
# 2. Verify the item number for that page is this number (261972139580)
# Print a success message if pass and raise an exception if fail.

from selenium import webdriver
import time

# Running a browser
driver = webdriver.Chrome()

# Assigning an URL
url = 'http://www.ebay.com'

# Sending the URL
driver.get(url)

# Detecting search field and pasting the value
search_fild = driver.find_element_by_id('gh-ac')
search_fild.send_keys('261972139580')

# Clicking the 'Search' button
search_button = driver.find_element_by_id('gh-btn')
search_button.click()

# Verifying by eBay item number
expected_eBay_item_number = 261972139581  # This is wrong value to fail the test. The correct one is 261972139580
time.sleep(4)
eBay_item_number = driver.find_element_by_id('descItemNumber')
number = eBay_item_number.text
print('=================')
print('=  %s =' % (number))
print('=================')

if int(number) == expected_eBay_item_number:
    print('Hooray! My first webdriver test passed')
else:
    raise Exception('Oops, something is wrong. Please review your code')
