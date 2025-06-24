from actions.create import add_new_task, view_tasks
from actions.menu import show_menu
from actions.remove import remove_tasks

# FUNCTIONS
def ask():
    reply_num = False
    while not reply_num:
        reply = input("Enter your choice: ")
        if reply.isnumeric():
            return reply
        else:
            reply_num = False
    return None


# INITIAL VARIABLES AND LISTS
tasks = []
on_off = True

# APP
while on_off:
    print("To-Do List Application")
    show_menu()
    choice = ask()
    if choice == "1":
        new_task = add_new_task()
        tasks.append(new_task)
        print(f"Task was added successfully")
        print()
    elif choice == "2":
        remove_tasks(tasks)
        print(f"Task was removed successfully")
        print()
    elif choice == "3":
        view_tasks(tasks)
        print()
    elif choice == "4":
        print("Goodbye")
        on_off = False
    else:
        print("Invalid choice")
        print()