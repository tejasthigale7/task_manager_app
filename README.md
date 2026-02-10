# 🗂️ Task Manager Application (Python)

A **console-based Task Manager Application** that helps users efficiently manage daily tasks by allowing them to **add, view, update, and delete tasks**.  
All tasks are **persistently stored in a JSON file**, ensuring data is preserved between program runs.

This project follows **professional software development practices**, including **object-oriented programming**, **modular architecture**, and **robust input validation**.

---

## 🚀 Features

- Add new tasks with name, description, and priority
- View all stored tasks in a clean, formatted list
- Update task details while retaining existing values
- Delete tasks with confirmation
- Persistent storage using JSON (`tasks.json`)
- Input validation using regular expressions
- Graceful error handling for invalid inputs and file issues
- Menu-driven command-line interface
- Modular and maintainable codebase

---

## 🧠 Key Concepts Applied

- Object-Oriented Programming (Classes & Objects)
- Modular code organization using packages
- File handling with JSON serialization/deserialization
- Input validation and error handling
- Data structures (lists and dictionaries)
- Conditional logic and loops
- String formatting

---

## 📂 Project Structure

task-manager-application-python/
│
├── data/
│ └── tasks.json # Persistent storage
│
├── task_manager_app/
│ ├── init.py # Package initializer
│ ├── task.py # Task model
│ ├── file_handler.py # File I/O logic
│ ├── input_validator.py # Input validation
│
├── main.py # Application entry point
└── README.md
