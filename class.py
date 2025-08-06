class Book:
    def __init__(self, name, page):
        self.pages = page
        self.name = name

    def open(self):
        print(f'opened the book {self.name} whit {self.pages} pages')


class Darsi(Book):
    def __init__(self, reshte, paye, name, page):
        Book.__init__(self, name, page)
        print('a new darsi book added')
        self.reshte = reshte
        self.paye = paye

    def open(self):
        print(f'book "{self.name}" for reshte {self.reshte} that has {self.pages} pages')


book_3 = Darsi('tajroby', 3, 'zist shenasi', 443)
book_3.open()
