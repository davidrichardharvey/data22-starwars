import requests
import json

# https://swapi.dev/api/starships/?page=1&format=json
# https://swapi.dev/api/starships/?page=2&format=json
# https://swapi.dev/api/starships/?page=3&format=json
# https://swapi.dev/api/starships/?page=4&format=json
# update read me,
# input request test is fine
# make sure collection is empty

response = requests.get("https://swapi.dev/api/people/?format=json")
response1 = requests.get("https://swapi.dev/api/starships/?page=1&format=json")    # 13, 14, 25, 31, 1, 9, 18, 19, 4
response2 = requests.get("https://swapi.dev/api/starships/?page=2&format=json")    # 22, 1, 13, 14, 29, 11, 35, 60, 39
response3 = requests.get("https://swapi.dev/api/starships/?page=3&format=json")    # 44, 10, 58, 35, 10, 11
response4 = requests.get("https://swapi.dev/api/starships/?page=4&format=json")    # 10, 35, 10, 11, 10, 79,

data = response1.text
parse = json.loads(data)
# print(parse)
# print(type(parse))
# print(response.status_code)

# y = parse["results"]
# for item in y:
#     if item["starships"]:  # show only available starships
#         print(item["name"], item["starships"])

y = parse["results"]
for item in y:
    if item["name"]:  # show only available starships
        print({item["name"]: item["pilots"]})


# As a user I want to replace all "pilots" keys with a list of ObjectIDs from characters collection
# return all pilots keys
# get all ObjectIDs
# create a list of ObjectIDs form characters collection
