import requests
import json


with open('reg_coordinates.json', mode='r', encoding='utf-8') as file:
    data = json.load(file, encoding='utf-8')[0]

for id in data:
    region = data[id][0]
    lat, lon = data[id][1][0], data[id][1][1]
    print(id, region, lat, lon)