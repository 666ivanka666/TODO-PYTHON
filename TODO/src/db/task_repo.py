from src.db.session import Session, create_session, Base
from src.db.model.task import Task



class TaskRepository:
    def __init__(self, session: Session):
        self.session = session

    def insert_task(self, task: Task):
        self.session.add(task)
        self.session.commit()

    def get_all_tasks(self):
        return self.session.query(Task).all()

    def get_task_by_id(self, task_id):
        return self.session.query(Task).filter(Task.id == task_id).first()

    def update_task(self, task: Task):
        self.session.commit()

    def delete_task(self, task: Task):
        self.session.delete(task)
        self.session.commit()

    def new_task(self, title, description, status):     
        task = Task(title=title, description=description, status=status)
        self.session.add(task)
        self.session.commit()
        print(f"Task created with ID {task.id}")
    
   
#tu su samo komande jer je ovo samo veza s bazom


