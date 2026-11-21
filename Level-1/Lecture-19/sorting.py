todos = [
     {
        "id": 1,
        "title": "Do python L-18 HW",
        "duration": 45,
        "completed": False
    }, 
   {
        "id": 2,
        "title": "Do math HW",
        "duration": 15,
        "completed": False
    }, 
   {
        "id": 3,
        "title": "Do english HW",
        "duration": 30,
        "completed": True
    }, 
     {
        "id": 4,
        "title": "Play outside",
        "duration": 60,
        "completed": True
    }, 
    {
        "id": 5,
        "title": "Wash dishes",
        "duration": 180,
        "completed": False
    }, 
]

todos.sort(key=lambda x: x["title"])
print(todos)