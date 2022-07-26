import requests
city=input("Enter your city name : ")
print(city)
print(f"The weather in {city} is ")
url='https://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)