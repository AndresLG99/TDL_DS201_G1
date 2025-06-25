from datetime import datetime
# ADD NEW TASKS FUNCTION

def add_new_task():
    priorities = ("Low", "Medium", "High")

    while True:
        task_title = input("Enter new task: ").strip()
        if task_title:
            break
        else:
            print("Task title cannot be empty. Please try again.")

    while True:
        try:
            task_priority = int(input(f"\nSet tasks's priority: \n1. Low\n2. Medium\n3. High\nEnter your choice: "))
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
    print(new_task["title"], "//", priorities[new_task["priority"]], "//", new_task["deadline"].date())
    print("=" * 50)

    return new_task

# CREATE VIEW TASKS FUNCTION

def view_tasks(tasks):
    for i in range(len(tasks)):
       print(f"{i+1}. {tasks[i]}")

# VIEW SORTED TASKS

priority_levels = ["LOW", "MEDIUM", "HIGH"]

def sort_key(task):
    p_index = priority_levels.index(task["Priority"]) # priority index
    y, m, d = task["Deadline"][0].split("-")    # deadline
    m_padded = m.zfill(2)   # one-two digits  "2025-6-5" → "2025-06-25"
    d_padded = d.zfill(2)   # one-two digits
    ymd_str = f"{y}-{m_padded}-{d_padded}"
    return p_index, ymd_str

tasks.sort(key=sort_key)

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")