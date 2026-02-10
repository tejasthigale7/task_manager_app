import re


def validate_string(prompt):
    """
    Validates non-empty string input.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def validate_priority(prompt):
    """
    Validates priority: High / Medium / Low
    """
    while True:
        value = input(prompt).strip().capitalize()
        if value in ["High", "Medium", "Low"]:
            return value
        print("Invalid priority. Please enter High, Medium, or Low.")


def validate_index(prompt, max_len):
    """
    Validates index input.
    """
    try:
        idx = int(input(prompt))
        if 1 <= idx <= max_len:
            return idx - 1
    except ValueError:
        pass

    print("Invalid task number.")
    return None
