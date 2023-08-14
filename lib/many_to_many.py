from datetime import datetime


class Author:
    all = []

    def __init__(self, name) -> None:
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(
            contract.royalties for contract in Contract.all if contract.author == self
        )


class Book:
    all = []

    def __init__(self, title) -> None:
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties) -> None:
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception(f"{value} is not a valid Book class")
        self._book = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception(f"{value} is not a valid author class")
        self._author = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        return sorted(
            cls.all,
            key=lambda contract: datetime.strptime(contract.date, "%m/%d/%Y"),
        )
