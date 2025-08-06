from library.library_book import LibraryBooks
from library.library_magazines import LibraryMags


lib = LibraryBooks()
mags = LibraryMags()


mags.show_mags()

lib.add_book("the Little Prince", "Antoine de Saint-Exupery")
lib.add_book("animal farm", "George Orwell")
lib.show_books()

lib.search_book("the Little Prince")
lib.remove_book("the Little Prince")
lib.show_books()
