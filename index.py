from actions.create import add_new_task
from actions.menu import show_menu
from actions.remove import remove_tasks
from actions.view import view_tasks
from actions.suggest_tasks import suggest_tasks
from utils import priorities
import datetime

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
# TODO: Uncomment and remove test
tasks = []
#tasks = [
#    {
#        'title': 'Taking out the trash',
#        'priority': 0, 'deadline': datetime.datetime(2025, 6, 27, 0, 0)
#    },
#    {
#        'title': 'Doing homework',
#        'priority': 1, 'deadline': datetime.datetime(2025, 6, 25, 0, 0)
#    },
#    {
#        'title': 'Getting coffee',
#        'priority': 0, 'deadline': datetime.datetime(2025, 6, 25, 0, 0)
#    }
#]

on_off = True
print("To-Do List Application")
# APP
while on_off:
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
        suggest_tasks(tasks)
        print()
    elif choice == "5":
        print("Goodbye")
        on_off = False
    else:
        print("Invalid choice")
        print()