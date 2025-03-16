import json
import os

data_file = "library.txt"

# Load the library from the file
def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

# Save the library to the file
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

# Add a book to the library
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully.")

# Remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ")
    initial_length = len(library)
    library = [book for book in library if book["title"].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found in the library.")

# Search for a book in the library
def search_library(library):
    search_by = input("Search by title, author, or genre: ").lower().strip()
    search_term = input(f"Enter the {search_by} to search for: ").lower().strip()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "Not Read"
            print(f"Title: {book['title']} - Author: {book['author']} - Year: {book['year']} - Genre: {book['genre']} - Read: {status}")
    else:
        print(f"No books found with {search_term} in {search_by}.")

# Display all books in the library
def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Not Read"
            print(f"Title: {book['title']} - Author: {book['author']} - Year: {book['year']} - Genre: {book['genre']} - Read: {status}")
    else:
        print("The library is empty.")

# Display statistics of the library
def display_statistics(library):
    total_books = len(library)
    read_books = sum([1 for book in library if book["read"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Main function to interact with the user
def main():
    library = load_library()
    while True:
        print("\nWelcome to the library manager")
        print("Menu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        

        

