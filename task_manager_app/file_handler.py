import json
import os
from task_manager_app.task import Task

DATA_FILE = "data/tasks.json"


def load_tasks():
    """
    Load tasks from JSON file.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(d) for d in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    """
    Save tasks to JSON file.
    """
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)
