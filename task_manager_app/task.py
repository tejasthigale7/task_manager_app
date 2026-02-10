class Task:
    """
    Task model representing a single task.
    """

    def __init__(self, name: str, description: str, priority: str):
        self.name = name
        self.description = description
        self.priority = priority

    # Convert object → dictionary (for JSON saving)
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority
        }

    # Convert dictionary → object (for JSON loading)
    @staticmethod
    def from_dict(data):
        return Task(
            data["name"],
            data["description"],
            data["priority"]
        )
