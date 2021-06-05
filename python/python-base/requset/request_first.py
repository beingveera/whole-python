import requests
from bs4 import BeautifulSoup
import html5lib 

url="https://www.facebook.com"

data=requests.get(url)
htmlcontent=data.content

#print(htmlcontent)

soup=BeautifulSoup(htmlcontent,'html.parser')

#print(soup)

title=soup.title 
#print(title.text)

header=soup.head
#print(header)


paras=soup.find_all('p')
#print(paras)


val=soup.find_all('a')
#print(val.text)


#print(soup.find('p')['class'])


#print(soup.find_all("p",class_="lead"))


#print(soup.find("p").get_text())

'''
for links in val:
    op=links.get('href')
    print(op)

'''

all_links=set()

'''
for links in val:
    if links.get("href") !='#':
        main_link="www.codewithharry.com" + links.get('href')
        all_links.add(main_link)
        print(main_link)

'''


