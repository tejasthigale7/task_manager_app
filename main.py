from task_manager_app.task import Task
from task_manager_app.file_handler import load_tasks, save_tasks
from task_manager_app.input_validator import (
    validate_string,
    validate_priority,
    validate_index
)


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.name} | {task.description} | {task.priority}")


def add_task(tasks):
    name = validate_string("Enter task name: ")
    description = validate_string("Enter description: ")
    priority = validate_priority("Enter priority (High/Medium/Low): ")

    tasks.append(Task(name, description, priority))
    save_tasks(tasks)

    print("Task added successfully!")


def update_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    display_tasks(tasks)
    idx = validate_index("Enter task number to update: ", len(tasks))

    if idx is None:
        return

    name = input("New name (leave blank to keep same): ").strip()
    desc = input("New description (leave blank to keep same): ").strip()
    pr = input("New priority (High/Medium/Low, blank to keep same): ").strip()

    if name:
        tasks[idx].name = name
    if desc:
        tasks[idx].description = desc
    if pr:
        tasks[idx].priority = pr.capitalize()

    save_tasks(tasks)

    print("Task updated successfully!")


def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    display_tasks(tasks)
    idx = validate_index("Enter task number to delete: ", len(tasks))

    if idx is None:
        return

    tasks.pop(idx)
    save_tasks(tasks)

    print("Task deleted successfully!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== Task Manager Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
