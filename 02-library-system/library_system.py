"""Library lending system LLD exercise — partially implemented module."""


class Book:
    def __init__(self, isbn, title, total_copies):
        self.isbn = isbn
        self.title = title
        self.total_copies = total_copies
        self.available_copies = total_copies

    def __repr__(self):
        return f"Book({self.title!r}, {self.available_copies}/{self.total_copies})"


class Member:
    MAX_BOOKS_PER_MEMBER = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.checked_out_isbns = []

    def has_reached_limit(self):
        """Whether this member already has MAX_BOOKS_PER_MEMBER books out.

        TODO: implement this — should be a simple comparison against
        len(self.checked_out_isbns).
        """
        raise NotImplementedError

    def has_checked_out(self, isbn):
        return isbn in self.checked_out_isbns


class Library:
    def __init__(self, catalog):
        """
        catalog: an iterable of Book instances the library owns.
        """
        self.catalog = {book.isbn: book for book in catalog}

    def find_book(self, isbn):
        """Look up a Book by ISBN.

        TODO: decide what to return when the ISBN isn't in the catalog.
        """
        raise NotImplementedError

    def checkout_book(self, member, isbn):
        """Check out a copy of the given title for `member`, if allowed.

        TODO: enforce all the rules from the README:
        - the title must exist in the catalog
        - there must be an available copy
        - the member must not already be at their borrowing limit
        - the member must not already have this title checked out
        Decide how to signal each failure case.
        """
        raise NotImplementedError

    def return_book(self, member, isbn):
        """Return the member's copy of the given title.

        TODO: put the copy back into the available pool and remove it
        from the member's checked-out list. Decide what should happen
        if the member never had this title checked out.
        """
        raise NotImplementedError
