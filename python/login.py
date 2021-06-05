from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()


browser.get('https://www.instagram.com/accounts/login/')


nm=browser.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input')
ps=browser.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input')
nm.send_keys()
ps.send_keys()

login_button = browser.find_element_by_css_selector('button[type=submit]').click()
login_button.click()

