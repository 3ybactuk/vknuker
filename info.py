import json

with open("options.json", "r") as file:
    data = json.load(file)

api_version = data["version"]

pwd = data["pass"]
user_id = data["user_id"]
user_login = data["login"]
