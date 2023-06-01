
from src.utils.input import create_input

def action_create(task_repo):
    title, description, status = create_input()
    task_repo.new_task(title, description, status)

def action_read(task_repo):
    try:
        task_id = int(input("Enter the ID of the task to read: "))
        task = task_repo.get_task_by_id(task_id)
        if task:
            print(task)
        else:
            print("Task not found.")
    except:
        print("We need number not string.")


def action_update(task_repo):
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = task_repo.get_task_by_id(task_id)
        if task:
            title, description, status = create_input()
            task.title = title
            task.description = description
            task.status = status
            task_repo.update_task(task)
            print("Task updated successfully.")
        else:
            print("Task not found.")
    except:
        print("We need number not string.")


def action_delete(task_repo):
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        task = task_repo.get_task_by_id(task_id)
        if task:
            task_repo.delete_task(task)
            print("Task deleted successfully.")
        else:
            print("Task not found.")
    except:
        print("We need number not string.")

def action_read_all(task_repo):
    tasks = task_repo.get_all_tasks()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

    
    
    
