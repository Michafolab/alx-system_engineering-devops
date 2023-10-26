#!/usr/bin/python3
''' Python script to export data in the JSON forma using REST API '''
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in todos]}, f)
