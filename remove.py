# REMOVE TASKS FUNCTION

def remove_task(tasks):
    choice = int(input("Enter the task to remove: "))
    tasks.pop(choice - 1)
    return tasks
