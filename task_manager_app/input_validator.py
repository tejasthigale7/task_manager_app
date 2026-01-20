
import re

PRIORITIES = {"high", "medium", "low"}


def validate_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def validate_priority(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in PRIORITIES:
            return value.capitalize()
        print("Invalid priority. Enter High, Medium, or Low.")


def validate_index(prompt, max_value):
    try:
        value = int(input(prompt))
        if 1 <= value <= max_value:
            return value - 1
    except ValueError:
        pass
    print("Invalid number.")
    return None
