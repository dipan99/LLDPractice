import pytest

from library_system import Book, Library, Member


def make_library():
    books = [
        Book("ISBN-1", "Dune", total_copies=2),
        Book("ISBN-2", "Foundation", total_copies=1),
        Book("ISBN-3", "Neuromancer", total_copies=1),
        Book("ISBN-4", "Snow Crash", total_copies=1),
    ]
    return Library(books)


# --- Member.has_reached_limit -----------------------------------------------

def test_member_has_not_reached_limit_when_empty():
    member = Member("M1", "Ada")
    assert not member.has_reached_limit()


def test_member_reaches_limit_at_max_books():
    member = Member("M1", "Ada")
    member.checked_out_isbns = ["a", "b", "c"]
    assert len(member.checked_out_isbns) == Member.MAX_BOOKS_PER_MEMBER
    assert member.has_reached_limit()


def test_member_under_limit_with_fewer_books():
    member = Member("M1", "Ada")
    member.checked_out_isbns = ["a"]
    assert not member.has_reached_limit()


# --- Library.find_book -------------------------------------------------------

def test_find_book_returns_the_book():
    library = make_library()
    book = library.find_book("ISBN-1")
    assert book is not None
    assert book.title == "Dune"


def test_find_book_returns_none_for_unknown_isbn():
    library = make_library()
    assert library.find_book("NOT-A-REAL-ISBN") is None


# --- Library.checkout_book ---------------------------------------------------

def test_checkout_book_reduces_available_copies():
    library = make_library()
    member = Member("M1", "Ada")

    library.checkout_book(member, "ISBN-1")

    assert library.find_book("ISBN-1").available_copies == 1
    assert "ISBN-1" in member.checked_out_isbns


def test_checkout_book_fails_when_no_copies_left():
    library = make_library()
    member1 = Member("M1", "Ada")
    member2 = Member("M2", "Grace")

    library.checkout_book(member1, "ISBN-2")  # only copy

    with pytest.raises(Exception):
        library.checkout_book(member2, "ISBN-2")


def test_checkout_book_fails_when_member_at_limit():
    library = make_library()
    member = Member("M1", "Ada")

    library.checkout_book(member, "ISBN-1")
    library.checkout_book(member, "ISBN-2")
    library.checkout_book(member, "ISBN-3")

    with pytest.raises(Exception):
        library.checkout_book(member, "ISBN-4")


def test_checkout_book_fails_on_duplicate_title():
    library = make_library()
    member = Member("M1", "Ada")

    library.checkout_book(member, "ISBN-1")

    with pytest.raises(Exception):
        library.checkout_book(member, "ISBN-1")


def test_checkout_book_fails_for_unknown_isbn():
    library = make_library()
    member = Member("M1", "Ada")

    with pytest.raises(Exception):
        library.checkout_book(member, "NOT-A-REAL-ISBN")


# --- Library.return_book ------------------------------------------------------

def test_return_book_restores_available_copies():
    library = make_library()
    member = Member("M1", "Ada")

    library.checkout_book(member, "ISBN-1")
    library.return_book(member, "ISBN-1")

    assert library.find_book("ISBN-1").available_copies == 2
    assert "ISBN-1" not in member.checked_out_isbns


def test_return_book_lets_another_member_checkout():
    library = make_library()
    member1 = Member("M1", "Ada")
    member2 = Member("M2", "Grace")

    library.checkout_book(member1, "ISBN-2")  # only copy
    library.return_book(member1, "ISBN-2")

    # should not raise now that the copy is back
    library.checkout_book(member2, "ISBN-2")
    assert "ISBN-2" in member2.checked_out_isbns
