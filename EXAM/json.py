import json5

data = {
    "name": "Bimal",
    "age": 22,
    "city": "berhampur",
    "interests": ["reading", "traveling", "coding"]
}

with open("data.json", "w") as json_file:
    json_file.write(json5.dumps(data))
with open("data.json", "r") as json_file:
    loaded_data = json5.load(json_file)

print("Loaded Data:")
print(loaded_data)
print("*************************************************************************")
print("Accessing Data Using Keys:")
print("Name:", loaded_data["name"])
print("Age:", loaded_data["age"])
print("City:", loaded_data["city"])
print("Interests:", loaded_data["interests"])
print("*************************************************************************")
print("All Keys:")
print(loaded_data.keys())
print("All Values:")
print(loaded_data.values())
print("*************************************************************************")
print("Modifying Data:")
loaded_data["age"] = 35
loaded_data["interests"].append("cooking")
print("Modified Data:")
print(loaded_data)
print("*************************************************************************")
print("Deleting Data:")
del loaded_data["city"]
print("Data after deletion:")
print(loaded_data)




