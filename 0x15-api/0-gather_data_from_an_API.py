#!/usr/bin/python3
""" Gathers data from an API """
import requests
from sys import argv

if __name__ == "__main__":
    emp_id = int(argv[1])
    query_str = "https://jsonplaceholder.typicode.com/todos/"
    todos = requests.get(query_str).json()
    total_tasks = len(todos)
    tasks_completed = 0
    titles_completed = []
    for task in todos:
        if task.get('userId') == emp_id and task.get('completed') is True:
            tasks_completed = tasks_completed + 1
            titles_completed.append(task.get('title'))

    query_users = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(query_users).json()
    for user in users:
        if user.get('id') == (emp_id):
            emp_name = user.get('name')

    print("Employee {} is done with tasks({}/{}):".format(emp_name,
          tasks_completed, total_tasks))
    for title in titles_completed:
        print("\t {}".format(title))
