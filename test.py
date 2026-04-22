import json

with open("data.json", 'r') as file:
    data = json.load(file)
    print(len(data["2024/2025"]))
    file.close()