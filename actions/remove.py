# REMOVE TASKS FUNCTION

def remove_tasks(tasks):
    choice = input("Enter the task to remove: ")
    while not choice.isnumeric():
        choice = input("Enter the task to remove: ")
    else:
        while int(choice) not in range(len(tasks)):
            choice = input("Enter the task to remove: ")
        else:
            tasks.pop(int(choice) - 1)
    return tasks