#!/usr/bin/env python3
# Test request to parse API's
import requests
import sys
import json


api_endpoint = "https://jsonplaceholder.typicode.com/"
user_id = sys.argv[1]
with requests.get(api_endpoint + "users/" + user_id) as response:
    json_data = response.json()
    employee_name = json_data.get('name')
with requests.get(api_endpoint + "users/" + user_id + "/todos") as response:
    json_data = response.json()
    total_num_of_tasks = len(json_data)
    completed_tasks = [todo for todo in json_data
                       if todo['completed'] is True]
    num_of_done_tasks = len(completed_tasks)
line_one = "Employee {} is done with \
tasks({}/{}):".format(employee_name, num_of_done_tasks, total_num_of_tasks)
print(line_one)
for task in completed_tasks:
    print("\t {}".format(task["title"]))
