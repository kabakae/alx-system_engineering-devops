#!/usr/bin/python3
"""
This module fetches TODO list progress for a given employee ID
using a REST API and prints the results in a specific format.
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch and display employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get employee information
    employee_url = f'{base_url}/users/{employee_id}'
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Get employee's TODO list
    todos_url = f'{base_url}/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to fetch TODO list for employee ID {employee_id}")
        return

    todos_data = todos_response.json()
