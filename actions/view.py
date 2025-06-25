from utils import priorities
# VIEW SORTED TASKS
def sort_tasks(tasks):
    return sorted(tasks, key=lambda task: (task["deadline"], task["priority"]))

def view_tasks(tasks):
    if len(tasks) > 0:
        sorted_tasks = sort_tasks(tasks)
        max_title_length = max(len(task["title"]) for task in tasks)

        print(f"{"ID":<3} | {"Task":<{max_title_length}} | {"Priority":<8} | {"Deadline":<12}")
        print("=" * (max_title_length + 30))
        for i, task in enumerate(sorted_tasks):
            print(f"{i+1:<3} | {task['title']:<{max_title_length}} | {priorities[task['priority']]:<8} | {task['deadline'].strftime('%Y-%m-%d'):<12}")
    else:
        print("Oops! No tasks were found.")
