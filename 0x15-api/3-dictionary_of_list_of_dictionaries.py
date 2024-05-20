import json
import requests

def fetch_data():
    # Fetching user data
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users_response.json()

    # Fetching tasks data
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = todos_response.json()

    # Creating the dictionary to hold all users' tasks
    tasks_dict = {}

    # Populating the dictionary with tasks for each user
    for user in users:
        user_id = user['id']
        username = user['username']
        tasks = [task for task in todos if task['userId'] == user_id]
        
        # Formatting the tasks for the user
        tasks_list = [{
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        } for task in tasks]
        
        tasks_dict[user_id] = tasks_list

    return tasks_dict

def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    data = fetch_data()
    export_to_json(data, "todo_all_employees.json")
