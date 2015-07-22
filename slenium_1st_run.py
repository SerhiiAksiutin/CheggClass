
from selenium import webdriver
import time

#Test case to go to amazon, search for a book and verify the price is the expected price.as


driver = webdriver.Chrome()

#going to amazon.com
url = 'http://www.amazon.com/'

driver.get(url)

#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')

#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()

#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()

#verifying rent price
expected_rent_price = 46.95 #this is the wrong price so expected to fail. Change it to the right price and watch it pass.

time.sleep(4)
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='

price = price.strip('$')

if float(price) != expected_rent_price:
    raise Exception('The price do not match')
else:
    print 'Yeyyyyyy the test passed'

"""
##########################################################
##################### console output #####################
##########################################################

In[12]: import selenium
In[13]: from selenium import webdriver
driver = webdriver.Chrome()
#going to amazon.com
url = 'http://www.amazon.com/'
driver.get(url)
#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')
#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()
#verifying rent price
expected_rent_price = 46.94
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='

Traceback (most recent call last):
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-13-db2fdd4cbbbc>", line 17, in <module>
    rent_price_element = driver.find_element_by_id('rentPrice')
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 197, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 681, in find_element
    {'using': by, 'value': value})['value']
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 164, in execute
    self.error_handler.check_response(response)
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/errorhandler.py", line 164, in check_response
    raise exception_class(message, screen, stacktrace)
NoSuchElementException: Message: u'no such element\n  (Session info: chrome=44.0.2403.89)\n  (Driver info: chromedriver=2.14.313457 (3d645c400edf2e2c500566c9aa096063e707c9cf),platform=Mac OS X 10.9.5 x86_64)'
In[14]: isbn_element = driver.find_element_by_xpath('//*[@id="productDetailsTable"]/tbody/tr/td/div/ul/li[4]')
In[15]: print isbn_element
<selenium.webdriver.remote.webelement.WebElement object at 0x10e8dcf90>
In[16]: type(isbn_element)
Out[16]: selenium.webdriver.remote.webelement.WebElement
In[17]: text = isbn_element.text
In[18]: print text
ISBN-10: 0321775651
In[19]: my_isbn_= isbn_element.text
In[20]: print my_isbn
Traceback (most recent call last):
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-20-7de7a893f6e8>", line 1, in <module>
    print my_isbn
NameError: name 'my_isbn' is not defined
In[21]: print my_isbn_
ISBN-10: 0321775651
In[22]: pic = driver.find_element_by_xpath('//*[@id="B00B03CLXK"]')
In[23]: pic.text
Out[23]: u''
In[24]: x = driver.find_element_by_xpath('//*[@id="books-entity-teaser"]/div/h2')
In[25]: x.text
Out[25]: u'More About the Authors'
In[26]: y = x.text
In[27]: print y
More About the Authors
In[28]: from selenium import webdriver
driver = webdriver.Chrome()
#going to amazon.com
url = 'http://www.amazon.com/'
driver.get(url)
#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')
#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()
#verifying rent price
expected_rent_price = 46.94
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='

Traceback (most recent call last):
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-28-db2fdd4cbbbc>", line 17, in <module>
    rent_price_element = driver.find_element_by_id('rentPrice')
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 197, in find_element_by_id
    return self.find_element(by=By.ID, value=id_)
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 681, in find_element
    {'using': by, 'value': value})['value']
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/webdriver.py", line 164, in execute
    self.error_handler.check_response(response)
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/selenium-2.39.0-py2.7.egg/selenium/webdriver/remote/errorhandler.py", line 164, in check_response
    raise exception_class(message, screen, stacktrace)
NoSuchElementException: Message: u'no such element\n  (Session info: chrome=44.0.2403.89)\n  (Driver info: chromedriver=2.14.313457 (3d645c400edf2e2c500566c9aa096063e707c9cf),platform=Mac OS X 10.9.5 x86_64)'
In[29]: rent_price_element = driver.find_element_by_id('rentPrice')
In[30]: price = rent_price_element.text
In[31]: print price
$46.94
In[32]: 46.94 == price
Out[32]: False
In[33]: price.strip('$')
Out[33]: u'46.94'
In[34]: price.strip()
Out[34]: u'$46.94'
In[35]: price = price.strip('$')
In[36]: price
Out[36]: u'46.94'
In[37]: print price
46.94
In[38]: 46.94 == price
Out[38]: False
In[39]: 46.94 == int(price)
Traceback (most recent call last):
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-39-01b91c014f2f>", line 1, in <module>
    46.94 == int(price)
ValueError: invalid literal for int() with base 10: '46.94'
In[40]: int(price)
Traceback (most recent call last):
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
    exec code_obj in self.user_global_ns, self.user_ns
  File "<ipython-input-40-c45be25e7a00>", line 1, in <module>
    int(price)
ValueError: invalid literal for int() with base 10: '46.94'
In[41]: 46.94 == float(price)
Out[41]: True
In[42]: price = price.strip('$')
if float(price) != 46.94:
    raise Exception('The price do not match')
else:
    print 'Yeyyyyyy the test passed'

Yeyyyyyy the test passed
In[43]: from selenium import webdriver
import time
driver = webdriver.Chrome()
#going to amazon.com
url = 'http://www.amazon.com/'
driver.get(url)
#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')
#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()
#verifying rent price
expected_rent_price = 46.94
time.sleep(4)
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='
price = price.strip('$')
if float(price) != 46.94:
    raise Exception('The price do not match')
else:
    print 'Yeyyyyyy the test passed'

=================
$46.94
=================
Yeyyyyyy the test passed
In[44]: from selenium import webdriver
import time
driver = webdriver.Chrome()
#going to amazon.com
url = 'http://www.amazon.com/'
driver.get(url)
#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')
#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()
#verifying rent price
expected_rent_price = 46.95
time.sleep(4)
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='
price = price.strip('$')
if float(price) != 46.94:
    raise Exception('The price do not match')
else:
    print 'Yeyyyyyy the test passed'

=================
$46.94
=================
Yeyyyyyy the test passed
In[45]: from selenium import webdriver
import time
driver = webdriver.Chrome()
#going to amazon.com
url = 'http://www.amazon.com/'
driver.get(url)
#finding the search field and typing the search term
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.send_keys('Campbell Biology')
#clicking the search button
search_button = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
search_button.click()
#clicking on the first search result
first_result = driver.find_element_by_xpath('//*[@id="result_0"]/div/div/div/div[1]/div/div/a/img')
first_result.click()
#verifying rent price
expected_rent_price = 46.95
time.sleep(4)
rent_price_element = driver.find_element_by_id('rentPrice')
price = rent_price_element.text
print '================='
print price
print '================='
price = price.strip('$')
if float(price) != expected_rent_price:
    raise Exception('The price do not match')
else:
    print 'Yeyyyyyy the test passed'

Traceback (most recent call last):
=================
  File "/Users/akinfu/virtualenvs/cheggtest/lib/python2.7/site-packages/ipython-1.1.0-py2.7.egg/IPython/core/interactiveshell.py", line 2827, in run_code
$46.94
    exec code_obj in self.user_global_ns, self.user_ns
=================
  File "<ipython-input-45-82d126a1e4e5>", line 26, in <module>
    raise Exception('The price do not match')
Exception: The price do not match
"""

"""
##########################################################
##################### Homework #####################
##########################################################
Problem 1
1. Go to ebay and search 261972139580
2. Verify the item number for that page is this number (261972139580
)
Print a success messege if pass and raise an exception if fail.

Problem 2 (optional)
Go to dice.com, search for qa job. click on any relult and print out the job description.
"""