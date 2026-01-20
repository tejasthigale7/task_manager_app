

import json
import os
from task_manager_app.task import Task

DATA_FILE = os.path.join("data", "tasks.json")


def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
