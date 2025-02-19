todo_list = []

def show_menu():
    print("\nTo Do List:")
    if not todo_list:
        print("No tasks available.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add Task")   
    print("2. Delete Task")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully.")

def delete_task():
    if not todo_list:
        print("No tasks to delete.")
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_task()
        elif choice == '2':
            delete_task()
        elif choice == '3':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
