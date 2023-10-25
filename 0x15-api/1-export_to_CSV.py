#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":
    import requests
    import sys
    import csv

    userId = sys.argv[1]

    # Fetch user information
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))
    user_data = user.json()
    user_name = user_data.get('username')

    # Fetch TODO tasks for the user
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos.json()

    # Prepare a list to hold the CSV rows
    csv_rows = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    for task in todos_data:
        if task.get('userId') == int(userId):
            task_completed = "completed" if task.get('completed') else "not completed"
            csv_row = [userId, user_name, task_completed, task.get('title')]
            csv_rows.append(csv_row)

    # Define the CSV file name based on the user ID
    filename = "{}.csv".format(userId)

    # Write the data to the CSV file
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_rows)

    print(f"Data exported to {filename}")
