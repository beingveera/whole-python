import requests
#r = requests.get('https://api.github.com/events')
#print(r)
#r = requests.post('https://httpbin.org/post', data = {'key':'value'})
#print(r)
#r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r=requests.delete('https://httpbin.org/delete')
print(r)