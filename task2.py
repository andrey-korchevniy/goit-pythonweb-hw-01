from abc import ABC, abstractmethod
from typing import List, Union
import logging


def run_task2() -> None:
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("task2")

    class Book:
        def __init__(self, title: str, author: str, year: Union[int, str]) -> None:
            self.title = title
            self.author = author
            self.year = year

        def __str__(self) -> str:
            return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    class LibraryInterface(ABC):
        @abstractmethod
        def add_book(self, title: str, author: str, year: Union[int, str]) -> None:
            pass

        @abstractmethod
        def remove_book(self, title: str) -> bool:
            pass

        @abstractmethod
        def show_books(self) -> None:
            pass

    class Library(LibraryInterface):
        def __init__(self) -> None:
            self.books: List[Book] = []

        def add_book(self, title: str, author: str, year: Union[int, str]) -> None:
            book = Book(title, author, year)
            self.books.append(book)

        def remove_book(self, title: str) -> bool:
            for book in self.books:
                if book.title == title:
                    self.books.remove(book)
                    return True
            return False

        def show_books(self) -> None:
            if not self.books:
                logger.info("No books in the library.")
                return

            for book in self.books:
                logger.info(str(book))

    class LibraryManager:
        def __init__(self, library: LibraryInterface) -> None:
            self.library = library

        def add_book(self, title: str, author: str, year: Union[int, str]) -> None:
            self.library.add_book(title, author, year)
            logger.info(f"Book '{title}' has been added.")

        def remove_book(self, title: str) -> None:
            result = self.library.remove_book(title)
            if result:
                logger.info(f"Book '{title}' has been removed.")
            else:
                logger.info(f"Book '{title}' not found.")

        def show_books(self) -> None:
            self.library.show_books()

    def main() -> None:
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
                    logger.info(
                        "Warning: Year should be a number. Storing as provided."
                    )
                manager.add_book(title, author, year)
            elif command == "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            elif command == "show":
                manager.show_books()
            elif command == "exit":
                break
            else:
                logger.info("Invalid command. Please try again.")

    main()


if __name__ == "__main__":
    run_task2()
