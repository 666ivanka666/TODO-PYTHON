from sqlalchemy import Column, Integer, String, DateTime, func
from src.db.session import Base


class Task(Base):
    __tablename__ = "Task"
    __table_args__ = {"sqlite_autoincrement": True}

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_date = Column(DateTime, default=func.now())  #moze i bez ovoga
  

    def __str__(self):
        return f"ID = {self.id}\nTitle = {self.title}\nDescription = {self.description}\nStatus = {self.status}\nCreated date = {self.created_date}"
