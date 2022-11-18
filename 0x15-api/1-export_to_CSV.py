#!/usr/bin/python3
''' Test request to parse API's
'''


import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        api_endpoint = "https://jsonplaceholder.typicode.com"
        user_id = sys.argv[1]
        user_data = requests.get(api_endpoint + "/users/" + user_id).json()
        employee_name = user_data.get('name')
        todo_data = \
            requests.get(api_endpoint + "/users/" + user_id + "/todos").\
            json()
        total_num_of_tasks = len(todo_data)
        completed_tasks = [todo for todo in todo_data
                           if todo['completed'] is True]
        num_of_done_tasks = len(completed_tasks)
        line_one = "Employee {} is done with tasks({}/{}):".format(
            employee_name,
            num_of_done_tasks,
            total_num_of_tasks)
        with open("{}.csv".format(user_id), 'w') as csv_file:
            todo_writer = csv.writer(csv_file, delimiter=",")
            for task in todo_data:
                todo_writer.writerow(['{}'.format(task["userId"]),
                                      '{}'.format(employee_name),
                                      '{}'.format(task['completed']),
                                      '{}'.format(task['title'])])
