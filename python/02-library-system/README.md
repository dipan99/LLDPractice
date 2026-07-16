# LLD Exercise: Library Lending System

**Difficulty:** Easy

## The setup

We're building a small system for a library to track book checkouts. Keep it simple — no floors, no branches, just one library with a catalog of books and a set of registered members.

Here's how it should behave:

- The library has a catalog of `Book` titles. Each title might have **multiple physical copies** — e.g. the library could own 3 copies of "Dune". Members check out a *copy* of a title, not a specific physical object, so you just need to track how many copies of a given title are currently available vs. checked out.
- Each `Member` has a **borrowing limit** — they can't have more than `MAX_BOOKS_PER_MEMBER` books checked out at once, across all titles.
- A member can't check out a book if there are no copies available.
- A member can't check out a title they've *already* checked out a copy of (no double-checkout of the same title — figure out how you want to detect that).
- When a book is returned, it should go back into the available pool for that title, and come off the member's checked-out list.

## What's already there

I've stubbed out a `library_system.py` module:

- `Book` — represents a title in the catalog, with total and available copy counts. Done.
- `Member` — a registered library member. Mostly done, but look at `has_reached_limit`.
- `Library` — the main system. This is where the real work is. A few methods are stubbed.

## What you need to build

1. `Library.checkout_book(member, isbn)` — check out a copy of the book with the given ISBN for the member, if allowed. If it's not allowed for *any* reason (no copies, limit reached, already has this title), you decide what should happen — I haven't told you whether to raise, return `False`, or something else. Just be consistent and make sure your tests (and mine) reflect whatever you pick.

2. `Library.return_book(member, isbn)` — return the member's copy of the given title. Think about what should happen if the member calls this for a book they never checked out.

3. `Library.find_book(isbn)` — look up a `Book` in the catalog by ISBN. I haven't told you what to return if it's not found.

## A note on the ambiguity

I've deliberately left open exactly *how* you signal failure cases (exceptions vs. sentinel return values vs. something else). Pick an approach, be consistent about it, and make sure it's easy for a caller to tell what happened.

## Running the tests

```bash
source ../../.venv/bin/activate   # from inside this folder
pytest test_library_system.py -v
```

Some tests will fail until you've filled in the stubs. That's the point.
