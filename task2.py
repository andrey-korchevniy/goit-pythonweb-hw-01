from abc import ABC, abstractmethod

def run_task2():
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
        
        def __str__(self):
            return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'
    
    class LibraryInterface(ABC):
        @abstractmethod
        def add_book(self, title, author, year):
            pass
        
        @abstractmethod
        def remove_book(self, title):
            pass
        
        @abstractmethod
        def show_books(self):
            pass
    
    class Library(LibraryInterface):
        def __init__(self):
            self.books = []

        def add_book(self, title, author, year):
            book = Book(title, author, year)
            self.books.append(book)

        def remove_book(self, title):
            for book in self.books:
                if book.title == title:
                    self.books.remove(book)
                    return True
            return False

        def show_books(self):
            if not self.books:
                print("No books in the library.")
                return
                
            for book in self.books:
                print(book)

    class LibraryManager:
        def __init__(self, library):
            self.library = library
            
        def add_book(self, title, author, year):
            self.library.add_book(title, author, year)
            print(f"Book '{title}' has been added.")
            
        def remove_book(self, title):
            result = self.library.remove_book(title)
            if result:
                print(f"Book '{title}' has been removed.")
            else:
                print(f"Book '{title}' not found.")
            
        def show_books(self):
            self.library.show_books()

    def main():
        library = Library()
        manager = LibraryManager(library)
        
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()
            
            if command == "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                try:
                    year = int(year)
                except ValueError:
                    print("Warning: Year should be a number. Storing as provided.")
                manager.add_book(title, author, year)
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            elif command == "show":
                manager.show_books()
            elif command == "exit":
                break
            else:
                print("Invalid command. Please try again.")

    main()

    
if __name__ == "__main__":
    run_task2()
