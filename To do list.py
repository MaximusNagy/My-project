tasks = []

def show_menu():
    print("--- To Do List ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ").strip().replace("\n", "")  # إزالة الأسطر الجديدة
        tasks.append(task)
        print("Task added successfully!")
    
    elif choice == "2":
        if tasks:
            print("--- Your Tasks ---")
            for i, task in enumerate(tasks, 1):
                # إزالة الأسطر الجديدة إذا كانت موجودة داخل كل مهمة
                task = task.replace("\n", " ")
                print(f"{i}. {task}")
        else:
            print("No tasks to show.")
    
    elif choice == "3":
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 0 < task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task removed: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
