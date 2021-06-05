from bs4 import BeautifulSoup
from requests import *
payload = {
    'action': 'login',
    'username': 'neha_lks',
    'password': '8107609895'
}

with session() as c:
   # c.post('https://www.instagram.com/login.php', data=payload)
    c.post('https://www.instagram.com/login.php',data=payload)
    response = c.get('https://www.instagram.com/accounts/edit/')
    print(response.headers)
    #print(response.text)