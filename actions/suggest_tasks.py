from actions.view import sort_tasks
from utils import priorities

def suggest_tasks(tasks):
    if len(tasks) < 1:
        print("Oops! No tasks were found.")
    else:
        print("=" * 50)
        print("Hey! You should start working on these tasks.")
        print("=" * 50)
        sorted_tasks = sort_tasks(tasks)
        max_title_length = max(len(task["title"]) for task in tasks)
        print(f"{"ID":<3} | {"Task":<{max_title_length}} | {"Priority":<8} | {"Deadline":<12}")
        print("=" * (max_title_length + 30))
        for i, task in enumerate(sorted_tasks[:2]):
            print(f"{i + 1:<3} | {task['title']:<{max_title_length}} | {priorities[task['priority']]:<8} | {task['deadline'].strftime('%Y-%m-%d'):<12}")
        print("=" * 50)



