# LLD Exercise: Vending Machine

**Difficulty:** Easy

## The setup

We want a little vending machine simulator. Nothing physical to worry about — just the logic of accepting coins, picking a product, and dispensing it (or not).

Here's how it should behave:

- The machine is stocked with products, each identified by a short code (like `"A1"`), and each with a price and a quantity on hand.
- A customer inserts coins one at a time, in whatever denominations the machine accepts. The machine keeps a running total of what's been inserted for the current transaction.
- The customer then selects a product by code.
  - If the code doesn't correspond to a real product, that's a failure case — figure out how you want to signal it.
  - If the product is out of stock, that's also a failure case.
  - If the customer hasn't inserted enough money yet, that's a failure case too — and importantly, their inserted coins should **not** be lost; they should still be able to add more coins and try again, or cancel.
  - If everything checks out: the product's stock goes down by one, the machine gives back the correct **change** (inserted amount minus price), and the running total resets to zero for the next transaction.
- The customer should also be able to cancel a transaction at any point and get back whatever they've inserted so far, with the running total resetting to zero.

## What's already there

I've stubbed out a small Swift package:

- `Coin` — an enum for the denominations the machine accepts. Done.
- `Product` — a simple value type for a slot's contents (name, price, quantity). Done.
- `VendingMachine` — the main type. Coin insertion is done; the selection and cancellation logic are stubbed out for you.

## What you need to build

1. The logic for handling a product selection — covering all the failure cases described above, and the successful-purchase path (decrement stock, compute and return change, reset the running total).
2. The logic for cancelling a transaction — refund whatever's been inserted and reset the running total.

I haven't told you exactly how failures should be surfaced (thrown errors, optionals, a result type — your call), just that the behavior needs to be correct and the state needs to stay consistent. Look at the test file to see the shape callers expect.

## Running the tests

```bash
cd 01-vending-machine
swift test
```

Some tests will fail until you've filled in the stubs. That's the point.
