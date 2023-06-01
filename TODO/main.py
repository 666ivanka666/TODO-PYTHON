from src.action.action import run_app
from src.db.session import init

if __name__ == "__main__":
    init()
    run_app()


