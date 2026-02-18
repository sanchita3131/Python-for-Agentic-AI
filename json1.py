import json

population_string = '''
{
  "people": [
    { "name": "Sunny", "age": 21, "city": "Delhi" },
    { "name": "Sanchita", "age": 19, "city": "Kolkata" }
  ]
}

'''

data=json.loads(population_string)


for person in data["people"]:
    del person["age"]

new_string=json.dumps(data)

print(new_string)

