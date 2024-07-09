import time

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed = []

    def add_task(self, task):
        self.tasks.append(task)
        self.completed.append(False)
        print(f"Added task: {task}")
        time.sleep(0.1)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.completed.pop(index)
            print(f"Removed task: {removed_task}")
            time.sleep(0.1)
        else:
            print("Invalid task index")
            time.sleep(0.1)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.completed[index] = True
            print(f"Completed task: {self.tasks[index]}")
            time.sleep(0.1)
        else:
            print("Invalid task index")
            time.sleep(0.1)

    def display_tasks(self):
        print("Displaying tasks...")
        time.sleep(0.1)
        if not self.tasks:
            print("No tasks in the list.")
            time.sleep(0.1)
        for i, task in enumerate(self.tasks):
            if self.completed[i]:
                status = "[x]"
            else:
                status = "[ ]"
            print(f"{i + 1}. {status} {task}")
            time.sleep(0.1)

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task, completed in zip(self.tasks, self.completed):
                file.write(f"{task},{completed}\n")
        print(f"Tasks saved to {filename}")
        time.sleep(0.1)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = []
                self.completed = []
                for line in file:
                    task, completed = line.strip().split(',')
                    self.tasks.append(task)
                    self.completed.append(completed == 'True')
            print(f"Tasks loaded from {filename}")
            time.sleep(0.1)
        except FileNotFoundError:
            print(f"File {filename} not found.")
            time.sleep(0.1)

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        time.sleep(0.1)
        print("1. Add Task")
        time.sleep(0.1)
        print("2. Remove Task")
        time.sleep(0.1)
        print("3. Complete Task")
        time.sleep(0.1)
        print("4. Display Tasks")
        time.sleep(0.1)
        print("5. Save Tasks")
        time.sleep(0.1)
        print("6. Load Tasks")
        time.sleep(0.1)
        print("7. Exit")
        time.sleep(0.1)
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter the filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.1)

if __name__ == "__main__":
    main()
