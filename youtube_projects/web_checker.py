from bs4 import *
import requests as rq 

url='http://lokesh-resume.web.app/'

c=rq.get(url)

html=c.text

soup=BeautifulSoup(html,'html.parser')

res=soup.find_all("div", class_="address")
print(str(res))