def suggest_tasks(tasks):
    print(tasks)
    sorted_lst = sorted(tasks, key=lambda task: task.deadline)
    print(tasks)
    print(sorted_lst)