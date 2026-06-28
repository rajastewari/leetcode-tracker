# creating a problem object
class Problem:
    def __init__(self, id, title, difficulty):
        self.id = id
        self.title = title
        self.difficulty = difficulty
        self.status = "todo"
        self.redo = False
        self.notes = ""

    # method to update the status of the problem
    def update_status(self, new_status):
        if new_status in ["todo", "in_progress", "done"]:
            self.status = new_status
        else:
            raise ValueError("Invalid status. Choose from 'todo', 'in_progress', or 'done'.")

    # __str__ method for printing object
    def __str__(self):
        redo_flag = " [REDO]" if self.redo else ""
        return f"[{self.id}] {self.title} ({self.difficulty}) - {self.status}{redo_flag}"

    # method to convert Problem object to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "difficulty": self.difficulty,
            "status": self.status,
            "redo": self.redo,
            "notes": self.notes
        }

    # method to create a Problem object from a dictionary
    @staticmethod
    def from_dict(data):
        problem = Problem(data["id"], data["title"], data["difficulty"])
        problem.status = data.get("status", "todo")
        problem.redo = data.get("redo", False)
        problem.notes = data.get("notes", "")
        return problem


