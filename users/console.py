import json


with open("alunos.json") as json_file:
    data = json.load(json_file)




print(data["dict"])
