import pytest

from parking_garage import (
    ParkingGarage,
    ParkingSpot,
    SpotSize,
    Vehicle,
    VehicleSize,
)


class FakeClock:
    """Controllable clock so tests can assert on fee calculation."""

    def __init__(self, start=0.0):
        self.now = start

    def __call__(self):
        return self.now

    def advance(self, seconds):
        self.now += seconds


def make_garage(clock):
    spots = [
        ParkingSpot("M1", SpotSize.MOTORCYCLE),
        ParkingSpot("C1", SpotSize.COMPACT),
        ParkingSpot("C2", SpotSize.COMPACT),
        ParkingSpot("L1", SpotSize.LARGE),
    ]
    return ParkingGarage(spots, time_fn=clock)


# --- ParkingSpot.can_fit ---------------------------------------------------

def test_motorcycle_fits_anywhere():
    bike = Vehicle("BIKE-1", VehicleSize.MOTORCYCLE)
    assert ParkingSpot("s", SpotSize.MOTORCYCLE).can_fit(bike)
    assert ParkingSpot("s", SpotSize.COMPACT).can_fit(bike)
    assert ParkingSpot("s", SpotSize.LARGE).can_fit(bike)


def test_compact_cannot_use_motorcycle_spot():
    car = Vehicle("CAR-1", VehicleSize.COMPACT)
    assert not ParkingSpot("s", SpotSize.MOTORCYCLE).can_fit(car)
    assert ParkingSpot("s", SpotSize.COMPACT).can_fit(car)
    assert ParkingSpot("s", SpotSize.LARGE).can_fit(car)


def test_large_vehicle_only_fits_large_spot():
    suv = Vehicle("SUV-1", VehicleSize.LARGE)
    assert not ParkingSpot("s", SpotSize.MOTORCYCLE).can_fit(suv)
    assert not ParkingSpot("s", SpotSize.COMPACT).can_fit(suv)
    assert ParkingSpot("s", SpotSize.LARGE).can_fit(suv)


# --- ParkingGarage.park_vehicle --------------------------------------------

def test_park_vehicle_picks_best_fit_spot():
    clock = FakeClock()
    garage = make_garage(clock)

    car = Vehicle("CAR-1", VehicleSize.COMPACT)
    ticket = garage.park_vehicle(car)

    assert ticket.spot.size == SpotSize.COMPACT
    assert ticket.spot.is_occupied
    assert ticket.vehicle is car


def test_park_vehicle_falls_back_to_larger_spot_when_needed():
    clock = FakeClock()
    garage = make_garage(clock)

    # fill both compact spots with compact cars first
    garage.park_vehicle(Vehicle("CAR-1", VehicleSize.COMPACT))
    garage.park_vehicle(Vehicle("CAR-2", VehicleSize.COMPACT))

    # a third compact car should now overflow into the large spot
    ticket = garage.park_vehicle(Vehicle("CAR-3", VehicleSize.COMPACT))
    assert ticket.spot.size == SpotSize.LARGE


def test_park_vehicle_raises_when_garage_is_full():
    clock = FakeClock()
    spots = [ParkingSpot("L1", SpotSize.LARGE)]
    garage = ParkingGarage(spots, time_fn=clock)

    garage.park_vehicle(Vehicle("SUV-1", VehicleSize.LARGE))

    with pytest.raises(Exception):
        garage.park_vehicle(Vehicle("SUV-2", VehicleSize.LARGE))


# --- ParkingGarage.unpark_vehicle ------------------------------------------

def test_unpark_vehicle_frees_the_spot():
    clock = FakeClock()
    garage = make_garage(clock)

    ticket = garage.park_vehicle(Vehicle("CAR-1", VehicleSize.COMPACT))
    spot = ticket.spot

    clock.advance(3600)  # 1 hour
    garage.unpark_vehicle(ticket)

    assert not spot.is_occupied


def test_unpark_vehicle_charges_for_elapsed_time():
    clock = FakeClock()
    garage = make_garage(clock)

    ticket = garage.park_vehicle(Vehicle("CAR-1", VehicleSize.COMPACT))
    clock.advance(3600 * 2)  # 2 hours parked

    fee = garage.unpark_vehicle(ticket)

    expected = 2 * ParkingGarage.RATE_PER_HOUR[SpotSize.COMPACT]
    assert fee == pytest.approx(expected)


# --- ParkingGarage.available_spot_count ------------------------------------

def test_available_spot_count_total():
    clock = FakeClock()
    garage = make_garage(clock)

    assert garage.available_spot_count() == 4

    garage.park_vehicle(Vehicle("CAR-1", VehicleSize.COMPACT))
    assert garage.available_spot_count() == 3


def test_available_spot_count_by_exact_size():
    clock = FakeClock()
    garage = make_garage(clock)

    assert garage.available_spot_count(SpotSize.COMPACT) == 2
    assert garage.available_spot_count(SpotSize.LARGE) == 1

    garage.park_vehicle(Vehicle("CAR-1", VehicleSize.COMPACT))
    assert garage.available_spot_count(SpotSize.COMPACT) == 1
    # parking a compact car should NOT reduce the large-spot count
    assert garage.available_spot_count(SpotSize.LARGE) == 1
