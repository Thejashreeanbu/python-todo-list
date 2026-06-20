tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print("Task added!")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")