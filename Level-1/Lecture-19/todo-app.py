options = """Options: 
1. add a todo 
2. display all the todos 
3. display single todo 
4. mark a todo as completed 
5. delete completed todo
6. exit 
"""
todos = {}
next_id = 1 
while True: 
    print("Todo Application: ")
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
            print("Adding a Todo: ")
            title = input("Title: ")
            todo = {
                "id": next_id,
                "title": title,
                "completed": False
            }
            todos[next_id] = todo.copy()
            next_id += 1 # moving to next id 
            print(f"Todo is added successfully")
        case 2: 
            print("Displaying all Todos:")
        case 3: 
            print("Displaying single Todo:")
        case 4: 
            print("Mark todo as completed: ")
        case 5: 
            print("Deleting completed todos: ")
        case 6: 
            print("Exiting..")
            break 
        case _: 
            print("Invalid choice")
    print("="*20)