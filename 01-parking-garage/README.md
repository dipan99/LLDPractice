# LLD Exercise: Parking Garage

**Difficulty:** Easy

## The setup

Alright, let's design a parking garage system. Nothing fancy — think of a single-level-ish garage (you don't need to model floors) that has a fixed number of spots, and those spots come in different sizes: `MOTORCYCLE`, `COMPACT`, and `LARGE`.

Vehicles also come in different sizes, and the sizing rules work how you'd expect in real life:

- A motorcycle can park in *any* spot (motorcycle, compact, or large).
- A compact car can park in a compact or large spot, but not a motorcycle spot.
- A large vehicle (think SUV / van) can only park in a large spot.

When a vehicle arrives, it should get parked in the *smallest available spot it fits in* — we don't want to waste a large spot on a motorcycle if a motorcycle spot is free. I'll leave it up to you exactly how you want to implement that "pick the best fit" logic, as long as the behavior holds.

## What's already there

I've stubbed out a `parking_garage.py` module with a few classes:

- `SpotSize` / `VehicleSize` — enums, already done.
- `ParkingSpot` — represents a single spot. Mostly done, but look closely at `can_fit`.
- `Vehicle` — a simple data holder. Done.
- `Ticket` — issued when a vehicle parks, used to unpark later. Partially done.
- `ParkingGarage` — the main thing you need to build out. This is where most of the stubs live.

## What you need to build

1. `ParkingGarage.park_vehicle(vehicle)` — find an appropriate spot (best fit, per the rules above), occupy it, and return a `Ticket`. If there's no valid spot available, figure out what makes sense to do (I haven't told you what exception or return value to use here — that's part of the exercise).

2. `ParkingGarage.unpark_vehicle(ticket)` — free up the spot associated with a ticket, and return the fee owed. Fee calculation is intentionally left vague below.

3. `ParkingGarage.available_spot_count(size=None)` — return how many spots are free. If a `size` is passed, only count free spots of *that exact* size (not "fits" — exact match).

## A note on the fee

I haven't specified a pricing model. There's a stubbed `RATE_PER_HOUR` dict on `ParkingGarage` keyed by `SpotSize` — you can use that, tweak it, or replace the approach entirely. Just make sure `unpark_vehicle` returns *some* numeric fee that's consistent with however long the vehicle was parked and reflects the tests' expectations. Look at the test file for the contract around timing — I'm not going to spell out how "elapsed time" gets fed into the system.

## Running the tests

```bash
source ../.venv/bin/activate   # from inside this folder
pytest test_parking_garage.py -v
```

Some tests will fail until you've filled in the stubs. That's the point.

Have fun — and don't overthink this one, it's meant to be a quick warm-up.
