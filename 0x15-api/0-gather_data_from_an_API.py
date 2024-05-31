#!/usr/bin/python3
"""python script to learn restAPI"""
import requests
import sys


def get_employee(resource):
	emp_url = "https://jsonplaceholder.typicode.com/"
	emp_url = emp_url + resource + sys.argv[1]
	employee = requests.get(emp_url)
	employee = employee.json()
	employee_name = employee['name']

	task_url = f"https://jsonplaceholder.typicode.com/todos/?userId={sys.argv[1]}"
	tasks = requests.get(task_url)
	task = tasks.json()
	print(len(task))



if __name__ == "__main__":
	get_employee("users/")
