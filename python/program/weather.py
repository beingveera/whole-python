import requests

city=input("Enter city name :")
print("\n")

url= ("https://api.openweathermap.org/data/2.5/weather?q={}&appid=22e369740b71c8ad33feb5539808e281".format(city))


json_data=requests.get(url). json()

for I in json_data:
	print(I, ' : ', json_data[I])
	print("\n")

