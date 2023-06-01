def create_input():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status: ")
    return title, description, status

def edit_input():
    title = input("Enter new title (or leave blank to skip): ")
    description = input("Enter new description (or leave blank to skip): ")
    status = input("Enter new status (or leave blank to skip): ")
    return title, description, status

def task_id_input():
    task_id = int(input("Enter task ID: "))
    return task_id

def crud_input():
     option = input("c-create, r-read, u-update, d-delete: ")
     return option