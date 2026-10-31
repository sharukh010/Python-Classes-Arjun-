## Practice Question: BookMyRead – Library Management System

Objective: Practice Python lists, list methods, and user-defined functions.

Create a menu-driven Python application called BookMyRead that allows users to manage books in a library.

### Initial Data

```
books = [    "Python Programming",    "Data Structures",    "Operating Systems",    "Computer Networks",    "Database Management"]
borrowed_books = []
returned_books = []
```

### Requirements

Create the following functions:

1\. `display_books()`

- Display all available books.
- Display each book with its corresponding ID (starting from 1).

2\. `borrow_book()`

- Display all available books.
- Ask the user to enter a book ID.
- Validate whether the entered ID is valid.
- Add the selected book to `borrowed_books`.
- Display an appropriate success or error message.

3\. `return_book()`

- Display all borrowed books.
- Ask the user to enter the book ID.
- Validate the entered ID.
- Remove the returned book from the borrowed_books 

4\. `display_borrowed_books()`

- Display all currently borrowed books.
- If there are no borrowed books, display `"No books borrowed"`.

5\. `display_returned_books()`

- Display all returned books.
- If there are no returned books, display `"No books returned"`.

### Menu

```
========== BOOKMYREAD ==========

1. Display Available Books
2. Borrow a Book
3. Return a Book
4. Display Borrowed Books
5. Display Returned Books
6. Exit

Enter your choice:
```

### Constraints

Try to solve the problem using the following Python list methods:

| List method | Purpose                       |
| ----------- | ----------------------------- |
| `append()`  | Add a book                    |
| `remove()`  | Remove a book                 |
| `pop()`     | Remove a book using its index |
| `extend()`  | Add multiple books            |
| `clear()`   | Clear a list                  |
| `index()`   | Find the position of a book   |
| `count()`   | Count occurrences             |

