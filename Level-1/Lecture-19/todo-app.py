options = """Options: 
1. add a todo 
2. display all the todos 
3. display single todo 
4. mark a todo as completed 
5. delete completed todo
6. exit 
"""
def display(todo: dict): 
    for key in todo: 
        print(f"{key.title()}: {todo[key]}")

todos = {
    1: {
        "id": 1,
        "title": "Do python L-18 HW",
        "completed": False
    }, 
    2: {
        "id": 2,
        "title": "Do math HW",
        "completed": False
    }, 
    3: {
        "id": 3,
        "title": "Do english HW",
        "completed": True
    }, 
    4: {
        "id": 4,
        "title": "Play outside",
        "completed": True
    }, 
    5: {
        "id": 5,
        "title": "Wash dishes",
        "completed": False
    }, 
}
next_id = 6
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
            print("1.Pending Todos")
            print("2.Completed Todos")
            sub_choice = int(input("Enter your choice: "))
            completed = None 
            if sub_choice == 1: 
                completed = False 
            else: 
                completed = True 

            for todo in todos.values():
                if todo["completed"] == completed: 
                    display(todo) 
                    print("-"*20)
        case 3: 
            print("Displaying single Todo:")
            todo_id = int(input("ID: "))
            if todo_id in todos: 
                display(todos[todo_id])
            else: 
                print("Todo not found")
        case 4: 
            print("Mark todo as completed: ")
            todo_id = int(input("ID: "))
            if todo_id in todos: 
                todo = todos[todo_id]
                todo["completed"] = True 
                print("Todo marked as completed...")
            else: 
                print("Todo not found")
        case 5: 
            print("Deleting completed todos: ")
            # it will get you all the ids completed todos 
            completed_ids = [todo_id for todo_id in todos if todos[todo_id]["completed"]]
            count = len(completed_ids)
            for todo_id in completed_ids: 
                del todos[todo_id]
            print(f"{count} Todos were deleted...")
        case 6: 
            print("Exiting..")
            break 
        case _: 
            print("Invalid choice")
    print("="*20)