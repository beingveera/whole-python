import requests as rq
url="https://www.google.com/"
#p=rq.get(url,auth=("user","pass"))
#print( p.headers)

#r=rq.post(url,data ={'key':'value'})
#print(r)
'''
l=rq.put(url,data ={'key':'value'})
print(l.content)

r = rq.put('https://httpbin.org/put', data = {'key':'value'})

p = rq.delete('https://httpbin.org/delete')

a = rq.head('https://httpbin.org/get')

n = rq.options('https://httpbin.org/get')

'''

#print(n.content)
#print(p.hearder)
#print(p.content)


payload = {'key1': 'value1', 'key2': 'value2'}
m = rq.get('https://httpbin.org/get', params=payload)


#print(m.url)
#print(m.text)
#a=m.json()
#print(a)

