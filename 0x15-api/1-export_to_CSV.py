#!/usr/bin/python3
""" Gathers data from an API """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = int(argv[1])
    api = "https://jsonplaceholder.typicode.com"
    user_details = requests.get("{}/users/{}".format(api, emp_id)).json()
    username = user_details.get('username')
    todos = requests.get("{}/todos".format(api)).json()

    with open("{}.csv".format(argv[1]), 'w') as f:
        for task in todos:
            if emp_id == task.get("userId"):
                f.write('"{}","{}","{}","{}"\n'.format(
                    argv[1],
                    username,
                    task.get('completed'),
                    task.get('title')))
