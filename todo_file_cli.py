# todo_file_cli.py

TASK_FILE = "tasks.txt"

# Load tasks from the file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"❗Error loading tasks: {e}")
        return []

# Save tasks to the file
def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"❗Error saving tasks: {e}")

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet!")
    else:
        print("📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    try:
        task = input("📝 Enter the new task: ").strip()
        if task:
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added!")
        else:
            print("⚠️ Task cannot be empty.")
    except Exception as e:
        print(f"❗Error adding task: {e}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = input("❌ Enter the task number to delete: ").strip()
        if not index.isdigit():
            raise ValueError("Not a number")
        index = int(index)
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
    except Exception as e:
        print(f"❗Error deleting task: {e}")

def run_todo_app():
    tasks = load_tasks()
    try:
        while True:
            show_menu()
            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                view_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("👋 Exiting To-Do App. Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n👋 Exiting due to keyboard interrupt.")
    except Exception as e:
        print(f"❗Unexpected error: {e}")

# Run the app
if __name__ == "__main__":
    run_todo_app()
