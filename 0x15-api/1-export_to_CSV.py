#!/usr/bin/python3
""" Gathers data from an API """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = int(argv[1])
    query_users = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(query_users).json()
    for user in users:
        if user.get('id') == (emp_id):
            emp_username = user.get('username')

    query_str = "https://jsonplaceholder.typicode.com/todos/"
    todos = requests.get(query_str).json()
    user_list = []
    for task in todos:
        tasks_list = [argv[1], emp_username]
        if task.get('userId') == emp_id:
            tasks_list.append(task.get('completed'))
            tasks_list.append(task.get('title'))
            user_list.append(tasks_list)
    filename = argv[1] + ".csv"
    with open(filename, 'w') as f:
        # creating a csv writer object
        csvwriter = csv.writer(f)
        csvwriter.writerows(user_list)
