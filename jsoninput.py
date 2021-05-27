import json


with open('doc.json') as f:
  data = json.load(f)

person_dict = json.loads(data)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

