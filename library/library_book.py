class LibraryBooks:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        print(f'Book "{title}" by {author} added')

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f'Book "{title} removed!')
                return
        print(f'Book "{title}" not found')

    def search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                print(f'found the "{book["title"]}" by {book["author"]}')
                return
        print(f'the "{title} was NOT found')

    def show_books(self):
        if not self.books:
            print("Library is empty of books")
        else:
            print("list of books:")
            for book in self.books:
                print(f'- {book["title"]} by {book["author"]}')
