# Creating a JSON file

import json5
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "interests": ["reading", "traveling", "coding"]
}

with open("data.json", "w") as json_file:
    json_file.write(json5.dumps(data))
