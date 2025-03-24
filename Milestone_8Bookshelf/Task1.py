class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"{self.title} by {self.author} (Category: {self.category})"


class Shelf:
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        self.books.add(book)

    def sort_books(self):
        self.books = sorted(self.books, key=lambda x: x.title)

    def __str__(self):
        return "\n".join(str(book) for book in self.books)


def organize_books(books):
    shelves = {}
    for book in books:
        if book.category not in shelves:
            shelves[book.category] = Shelf()
        shelves[book.category].add_book(book)
    return shelves


books = {
    Book("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("1984", "George Orwell", "Dystopian"),
    Book("Brave New World", "Aldous Huxley", "Dystopian"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Classic")
}

shelves = organize_books(books)

for category, shelf in shelves.items():
    shelf.sort_books()

for category, shelf in shelves.items():
    print(f"Category: {category}")
    print(shelf)
    print()