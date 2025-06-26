from actions.create import add_new_task
from actions.menu import show_menu
from actions.remove import remove_tasks
from actions.view import view_tasks
from actions.suggest_tasks import suggest_tasks
from art import *
import datetime

# FUNCTIONS
def ask():
    while True:
        try:
            reply = int(input("Enter your choice: "))
            if reply in [1, 2, 3, 4, 5]:
                return reply
            else:
                print("Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# INITIAL VARIABLES AND LISTS
# TODO: Uncomment and remove test
# tasks = []
tasks = [
    {
        'title': 'Taking out the trash',
        'priority': 0, 'deadline': datetime.datetime(2025, 6, 27, 0, 0)
    },
    {
        'title': 'Doing homework',
        'priority': 1, 'deadline': datetime.datetime(2025, 6, 25, 0, 0)
    },
    {
        'title': 'Getting coffee',
        'priority': 0, 'deadline': datetime.datetime(2025, 6, 25, 0, 0)
    }
]

on_off = True
print("=" * 100)
tprint("TO  DO  LIST APP")
print("=" * 100)

while on_off:
    show_menu()
    choice = ask()
    print("=" * 100)
    if choice == 1:
        print("# ADD NEW TASK #")
        print("=" * 100)
        new_task = add_new_task()
        tasks.append(new_task)
    elif choice == 2:
        print("# REMOVE TASK #")
        print("=" * 100)
        tasks = remove_tasks(tasks)
    elif choice == 3:
        print("# VIEW TASKS #")
        print("=" * 100)
        view_tasks(tasks)
    elif choice == 4:
        print("# SUGGEST TASKS #")
        print("=" * 100)
        suggest_tasks(tasks)
    elif choice == 5:
        tprint("BYE BYE")
        on_off = False
    print("=" * 100)