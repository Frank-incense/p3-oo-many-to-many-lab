class Author:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]
    
    def books(self):
        return [book.book for book in Contract.all if self == book.author]
    
    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
           return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        royalties = 0
        for contract in Contract.all:
            if self == contract.author:
                royalties += contract.royalties
        return royalties
    

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
    
    def authors(self):
        return [book.author for book in Contract.all if self == book.book]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and \
            isinstance(book, Book) and \
            isinstance(date, str) and\
            isinstance(royalties, int):
            self.author = author
            self.book = book
            self.royalties = royalties
            self.date = date
            type(self).all.append(self)

        else:
            raise Exception("Author and book must be objects")
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if date == contract.date]