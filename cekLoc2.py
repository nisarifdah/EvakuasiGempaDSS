import requests

r = requests.get('https://get.geojs.io/')

ip_requests = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_requests.json()['ip']
##print(ipAdd)

url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_requests = requests.get(url)
geo_data = geo_requests.json()

print(geo_data['latitude'])
print(" ")
print(geo_data['longitude'])
print(" ")
print(geo_data['city'])