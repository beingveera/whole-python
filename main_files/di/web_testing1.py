import selenium 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Edge('C:\\Users\\techno\\Downloads\\msedgedriver.exe')



name='Lokesh'
phone='9829237552'
mail='veera@gmail.com'
mess='its mee veera with automation python'


driver.get('https://veera.site123.me/contact')
time.sleep(0.2)

putt=driver.find_element_by_name('contact_name')
putt.send_keys(name)

putt1=driver.find_element_by_name('contact_phone')
putt1.send_keys(phone)

putt2=driver.find_element_by_name('contact_email')
putt2.send_keys(mail)

putt3=driver.find_element_by_name('contact_message')
putt3.send_keys(mess)

submit=driver.find_elements_by_tag_name('button')
submit.click()

time.sleep(0.3)

print('Done...')







