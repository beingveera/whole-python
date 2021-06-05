import requests 
from bs4 import * 

url="https://github.com/techno-veera?tab=repositories"
res=requests.get(url)

ls=res.text

soup=BeautifulSoup(ls,'html.parser')
my=soup.find('div',class_="h-card mt-md-n5")
print(my)