class LibraryMags:
    def __init__(self):
        self.magazines = []

    def add_mag(self, title, publisher, number):
        self.magazines.append({'title': title, 'author': publisher, 'number': number})
        print(f'magazine "{title}" number {number} by {publisher} added')

    def remove_mag(self, title):
        for mag in self.magazines:
            if mag['title'] == title:
                self.magazines.remove(mag)
                print(f'magazine "{title}" removed!')
                return
        print(f'magazine "{title}" not found')

    def search_mag(self, title):
        for mag in self.magazines:
            if mag['title'] == title:
                print(f'found the "{mag["title"]}" number {mag["number"]} by {mag["author"]}')
                return
        print(f'the "{title}" was NOT found')

    def show_mags(self):
        if not self.magazines:
            print("Library is empty of magazines")
        else:
            print("list of magazines:")
            for book in self.magazines:
                print(f'- {book["title"]} by {book["author"]}')
