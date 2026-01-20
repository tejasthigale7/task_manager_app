

from task_manager_app.task import Task
from task_manager_app.file_handler import load_tasks, save_tasks
from task_manager_app.input_validator import (
    validate_string,
    validate_priority,
    validate_index
)


def display_menu():
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task.name} | {task.description} | Priority: {task.priority}")


def add_task(tasks):
    name = validate_string("Enter task name: ")
    description = validate_string("Enter description: ")
    priority = validate_priority("Enter priority (High/Medium/Low): ")

    tasks.append(Task(name, description, priority))
    save_tasks(tasks)
    print(f"Task '{name}' added successfully!")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    index = validate_index("Enter task number to update: ", len(tasks))
    if index is None:
        return

    task = tasks[index]

    new_name = input("New name (leave blank to keep): ").strip()
    new_desc = input("New description (leave blank to keep): ").strip()
    new_priority = input("New priority (High/Medium/Low, blank to keep): ").strip()

    if new_name:
        task.name = new_name
    if new_desc:
        task.description = new_desc
    if new_priority:
        task.priority = validate_priority("Confirm priority: ")

    save_tasks(tasks)
    print(f"Task '{task.name}' updated successfully!")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    index = validate_index("Enter task number to delete: ", len(tasks))
    if index is None:
        return

    confirm = input("Are you sure? (y/n): ").lower()
    if confirm == "y":
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Task '{removed.name}' deleted successfully!")
    else:
        print("Deletion cancelled.")


def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
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
