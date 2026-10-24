options = """Options: 
1) Add a moive
2) Display all the movies 
3) Delete a movie 
4) Exit"""
movies = [] 
while True: 
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
            print("Adding a moive: ")
            name = input("Name: ")
            movies.append(name)
        case 2: 
            print("Movies: ")
            for index in range(len(movies)): 
                print(f"{index+1}. {movies[index]}")
        case 3: 
            print("Deleting a movie: ")
            movie_id = int(input("ID: "))
            if movie_id <= len(movies): 
                movies.pop(movie_id-1)
            else: 
                print("Invalid Movie ID")
        case 4: 
            print("Exiting...")
            break 
        case _ : 
            print("Invalid input")