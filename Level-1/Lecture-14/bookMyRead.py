books = ["Python Programming",
        "Data Structures",
        "Operating Systems",
        "Computer Networks",
        "Database Management"]
borrowed_books = []
returned_books = []

def display_available_books(): 
    if len(books) == 0: 
        print("No Available Books..")
    else: 
        for i in range(len(books)): 
            print(f"{i+1}. {books[i]}")

def borrow_book(bid): 
    book = books.pop(bid-1)
    borrowed_books.append(book)

def return_book(bid): 
    book = borrowed_books.pop(bid-1)
    returned_books.append(book)
    books.append(book)

def display_borrowed_books(): 
    if len(borrowed_books) == 0: 
        print("No books Borrowed..")
    else: 
        for i in range(len(borrowed_books)): 
            print(f"{i+1}. {borrowed_books[i]}")

def display_returned_books(): 
    if len(returned_books) == 0: 
        print("No books Returned..")
    else: 
        for i in range(len(returned_books)): 
            print(f"{i+1}. {returned_books[i]}")
while True: 
    print("""========== BOOKMYREAD ==========

    1. Display Available Books
    2. Borrow a Book
    3. Return a Book
    4. Display Borrowed Books
    5. Display Returned Books
    6. Exit
    """)
    choice = int(input("Enter your choice (1-6): "))
    match choice: 
        case 1: 
            print("Available Books: ")
            display_available_books()
        case 2: 
            print("Borrow a Book: ")
            bid = int(input("Book ID: "))
            # bid is BOOK ID 
            if bid <= 0 or bid > len(books): 
                print("Invalid Book ID")
            else: 
                borrow_book(bid)
                print("Borrowed book...")
        case 3: 
            print("Return a Book: ")
            bid = int(input("Book ID: "))
            if bid <= 0 or bid > len(borrowed_books): 
                print("Invalid Book ID")
            else: 
                return_book(bid)
                print("Returned Book..")
        case 4: 
            print("Borrowed Books: ")
            display_borrowed_books()
        case 5: 
            print("Returned Books: ")
            display_returned_books()
        case 6: 
            print("Exiting..")
            break 
        case _ : 
            print("Invalid input. Try again")
    print("="*20)