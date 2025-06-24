menu = ["Add task", "Remove task", "View tasks", "Exit"]

def show_menu():
    for item in range(len(menu)):
        print(f"{item + 1}. {menu[item]}")
