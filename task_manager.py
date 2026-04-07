tasks = []                              # Task Manager Program 
while True:
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":                       # Add Task
        task = input("Enter task: ")
        tasks.append([task, "Not Done"])
        print("Task added")
    elif choice == "2":                      # Show Tasks              
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            i = 1
            for t in tasks:
                print(i, ".", t[0], "-", t[1])
                i += 1
    elif choice == "3":                             # Mark Task Done
        num = int(input("Enter task number: "))
        if num <= len(tasks):
            tasks[num-1][1] = "Done"
            print("Task completed")
        else:
            print("Invalid number")
    elif choice == "4":                              # Delete Task
        num = int(input("Enter task number: "))
        if num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted")
        else:
            print("Invalid number")
    elif choice == "5":                                # Exit
        print("Program closed")
        break
    else:
        print("Wrong choice")