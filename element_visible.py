"""
Write a function called element_visible that will check
if an element is visible on the page and returns True or False.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Running browser >
driver = webdriver.Firefox()

# Maximizing the browser >
driver.maximize_window()

# Assigning the URL >
url = 'http://www.chegg.com/schools'

# Opening the URL >
driver.get(url)

# Assigning the keyword >
keyword = 'art'

# Finding the search field >
search_field = driver.find_element_by_id('schools-search-input')

# Sending the keyword
search_field.send_keys(keyword)
search_field.send_keys(Keys.RETURN)

# Verifying visibility
driver.implicitly_wait(10)


def visibility():
    hidden = driver.find_element_by_xpath(
      'html/body/div[2]/div[5]/div[2]/div[1]/a')
    if hidden.is_displayed():
        print('Element is visible')
        return hidden.is_displayed()
    else:
        print('Element is not visible')
        return hidden.is_displayed()
print(visibility())
