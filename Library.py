from rich import print
from rich.console import Console
from datetime import datetime

console = Console()

class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    # a. List Books
    def list_books(self):
        self.file.seek(0) 
        books = self.file.readlines()
        if not books:
            console.print("No books available.", style="bold red")
            return
        console.print("List of Books:", style="bold green")
        for book in books:
            book_info = book.strip().split(',')
            console.print(f"Title: [blue]{book_info[0]}[/blue], Author: [blue]{book_info[1]}[/blue]")

    # b. Add Book
    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        num_pages = input("Enter the number of pages of the book: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        console.print("Book added successfully.", style="bold green")

    # c. Remove Book
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        found = False
        for book in books:
            if title in book:
                found = True
                continue
            new_books.append(book)
        if not found:
            console.print("Book not found.", style="bold red")
            return
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_books)
        console.print("Book removed successfully.", style="bold green")

    def welcome_message(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.file.seek(0)
        books = self.file.readlines()
        book_count = len(books)
        console.print(f"\nWelcome to the Library Management System!", style="bold blue")
        console.print(f"Current time: [cyan]{current_time}[/cyan]")
        console.print(f"Total Books in Library: [cyan]{book_count}[/cyan]\n")

# Create Library object
lib = Library()
lib.welcome_message()

# Menu
while True:
    console.print("[bold cyan]*** MENU ***[/bold cyan]")
    console.print("1) List Books")
    console.print("2) Add Book")
    console.print("3) Remove Book")
    console.print("4) Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        console.print("Invalid choice. Please choose again.", style="bold red")
