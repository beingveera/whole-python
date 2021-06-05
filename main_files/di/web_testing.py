import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Edge("C:\\Users\\techno\\Downloads\\msedgedriver.exe")
driver.get('https://python.org')
#print(driver.title)

search=driver.find_element_by_name('q')
search.clear()
search.send_keys('getting start with python')
search.send_keys(Keys.RETURN)


print(driver.current_url)


driver.close()