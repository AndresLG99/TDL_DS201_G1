from actions.view import view_tasks, sort_tasks
# REMOVE TASKS FUNCTION

def remove_tasks(tasks):
    view_tasks(tasks)
    sorted_tasks = sort_tasks(tasks)
    print()

    while True:
        try:
            choice = int(input(f"Enter the ID of the task to remove (1 - {len(sorted_tasks)}) / 0: Cancel \n"))
            if choice in range(0, len(sorted_tasks)+1):
                if choice == 0:
                    print(f"Aborting")
                    break
                else:
                    sorted_tasks.pop(choice - 1)
                    print(f"Task was removed successfully")
                    break
            else:
                print(f"Please enter a number from 0 to {len(sorted_tasks)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return sorted_tasks