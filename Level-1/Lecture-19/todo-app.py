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
            for todo in todos.values():
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
        case 5: 
            print("Deleting completed todos: ")
        case 6: 
            print("Exiting..")
            break 
        case _: 
            print("Invalid choice")
    print("="*20)