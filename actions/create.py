# ADD NEW TASKS FUNCTION

def add_new_task():
    new_task = input("Enter new task: ")
    return new_task

# CREATE VIEW TASKS FUNCTION

def view_tasks(tasks):
    for i in range(len(tasks)):
       print(f"{i+1}. {tasks[i]}")
