import json

class ToDoList:
    def __init__(self, filename="todolist.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid index.")

def print_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(index)

        elif choice == "4":
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)

        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
