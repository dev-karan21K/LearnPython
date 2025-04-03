#todo applications

tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully")
    
    
def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter a number: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed successfully")
    except (IndexError, ValueError):
        print("Invalid Task number.")


def show_tasks():
    if not tasks:
        print("\n no task in the list.")
    else:
        print("\n your task: ")
        for i, task in enumerate(tasks, start=1):
            print(i, task)


def main():
    while True:
        print("\nOptions: 1. Add Task 2. Remove Task 3. Show Task 4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exitign todo-list bye!") 
            break
        else:
            print("Invalid Choice, try again!")
        
main()