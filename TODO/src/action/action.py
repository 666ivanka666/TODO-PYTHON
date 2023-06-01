
from src.db.task_repo import TaskRepository
from src.db.session import create_session
from src.utils.action import action_create, action_delete, action_read, action_update, action_read_all


def run_app():
    session = create_session()
    task_repo = TaskRepository(session)



    while True:
        action = input("c-create, r-read, u-update, d-delete, ra-read all: ")

        if action == "c":
            action_create(task_repo)
        elif action == "r":
            action_read(task_repo)
        elif action == "u":
            action_update(task_repo)
        elif action == "d":
            action_delete(task_repo)
        elif action == "ra":
            action_read_all(task_repo)
        else:
            break