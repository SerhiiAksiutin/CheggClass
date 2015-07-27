# Problem 1
# 1. Go to ebay and search 261972139580
# 2. Verify the item number for that page is this number (261972139580)
# Print a success message if pass and raise an exception if fail.

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Running a browser >
driver = webdriver.Chrome()

# Maximizing the browser >
driver.set_window_size(1280, 800)
driver.set_window_position(0, 0)

# Assigning an URL >
url = 'http://www.ebay.com'

# Sending the URL >
driver.get(url)

# Detecting search field and pasting the value >
search_field = driver.find_element_by_id('gh-ac')
search_field.send_keys('261972139580')

# Clicking the 'Search' button >
# search_button = driver.find_element_by_id('gh-btn')
# search_button.click()

# Pressing Enter >
search_field.send_keys(Keys.RETURN)

# Verifying by eBay item number >
expected_eBay_item_number = 261972139580

# Explicit waiting >
wait = WebDriverWait(driver, 4)
elem = wait.until(EC.presence_of_element_located((By.ID, 'descItemNumber')))

# Finding and printing the item number >
eBay_item_number = driver.find_element_by_id('descItemNumber')
number = eBay_item_number.text
print('=================')
print('=  %s =' % (number))
print('=================')

# Raisign en error once the item mumber doesn't match >
if int(number) == expected_eBay_item_number:
    print('Hooray! My first webdriver test has passed')
else:
    raise Exception('Oops, something is wrong. Please review your code')
