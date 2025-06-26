from datetime import datetime
from utils import priorities
# ADD NEW TASKS FUNCTION

def add_new_task():

    while True:
        task_title = input("Enter new task: ").strip()
        if task_title:
            break
        else:
            print("Task title cannot be empty. Please try again.")

    while True:
        try:
            task_priority = int(input(f"Set tasks' priority: \n1. High\n2. Medium\n3. Low\nEnter your choice: "))
            if task_priority in [1, 2, 3]:
                break
            else:
                print("Please enter a number from 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        task_deadline = input("Enter a deadline (YYYY-MM-DD): ")
        try:
            task_deadline = datetime.strptime(task_deadline, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid format. Please enter the date as YYYY-MM-DD.")

    new_task = {
        "title": task_title,
        "priority": task_priority-1,
        "deadline": task_deadline,
    }

    print("=" * 50)
    print("Task:", new_task["title"])
    print("Priority:", priorities[new_task["priority"]])
    print("Date:", new_task["deadline"].date())
    print(f"Task was added successfully!")

    return new_task

# CREATE VIEW TASKS FUNCTION

def view_tasks(tasks):
    for i in range(len(tasks)):
       print(f"{i+1}. {tasks[i]}")

