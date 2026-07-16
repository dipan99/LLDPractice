"""Parking garage LLD exercise — partially implemented module."""

import itertools
import time
from enum import Enum


class SpotSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class Vehicle:
    def __init__(self, license_plate, size):
        self.license_plate = license_plate
        self.size = size

    def __repr__(self):
        return f"Vehicle({self.license_plate!r}, {self.size.name})"


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.vehicle = None

    @property
    def is_occupied(self):
        return self.vehicle is not None

    def can_fit(self, vehicle):
        """Whether `vehicle` is allowed to park here.

        TODO: implement the sizing rules described in the README —
        a vehicle can use a spot of its own size or larger.
        """

        if not self.is_occupied and self.size.value >= vehicle.size.value:
            return True
        return False

    def occupy(self, vehicle):
        self.vehicle = vehicle

    def vacate(self):
        self.vehicle = None


class Ticket:
    _id_counter = itertools.count(1)

    def __init__(self, vehicle, spot, entry_time):
        self.ticket_id = next(Ticket._id_counter)
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = entry_time
        self.exit_time = None

    # TODO: you may end up wanting a method here to mark the ticket
    # closed out (exit_time set) when the vehicle unparks. Or you might
    # decide ParkingGarage should own that instead — your call.

    def close(self, time):
        self.spot.vacate()
        self.exit_time = time


class ParkingGarage:
    # Placeholder pricing — tweak as you see fit, or replace the model.
    RATE_PER_HOUR = {
        SpotSize.MOTORCYCLE: 2.0,
        SpotSize.COMPACT: 4.0,
        SpotSize.LARGE: 6.0,
    }

    def __init__(self, spots, time_fn=time.time):
        """
        spots: an iterable of ParkingSpot instances to seed the garage with.
        time_fn: a zero-arg callable returning the current time (as a float,
            seconds). Defaults to time.time, but tests will likely pass
            their own fake clock so elapsed-time math is deterministic.
        """
        self.spots = list(spots)
        self._time_fn = time_fn
        self._active_tickets = {}  # ticket_id -> Ticket

    def park_vehicle(self, vehicle):
        """Find the best-fit available spot for `vehicle`, occupy it,
        and return a Ticket.

        TODO: "best fit" means the smallest spot (by SpotSize) that the
        vehicle can legally use — see can_fit and the README.
        Decide what should happen if no spot is available.
        """

        # i have a list of spots
        # find the best fit
        # occupy
        # return Ticket



        best_fit = None

        for spot in self.spots:
            if spot.can_fit(vehicle):
                best_fit = spot
                break
              
        
        if not best_fit:
            raise Exception("No spot available for this vehicle")
        
        for spot in self.spots:
            if spot.can_fit(vehicle):
                if spot.size.value < best_fit.size.value:
                    best_fit = spot
        
        best_fit.occupy(vehicle)
        ticket = Ticket(vehicle, best_fit, self._time_fn())
        self._active_tickets[ticket.ticket_id] = ticket
        return ticket
        

    def unpark_vehicle(self, ticket):
        """Free the spot associated with `ticket` and return the fee owed.

        TODO: use self._time_fn() to determine how long the vehicle was
        parked, and RATE_PER_HOUR (or your own pricing) to compute the fee.
        """

        # spot = ticket.spot
        # spot.vacate()

        ticket.close(self._time_fn())

        time_occupied = (ticket.exit_time - ticket.entry_time) / 3600

        hourly_rate = self.RATE_PER_HOUR[ticket.spot.size]

        total_rate = time_occupied * hourly_rate

        return total_rate


        # raise NotImplementedError

    def available_spot_count(self, size=None):
        """Return the number of free spots.

        TODO: if `size` is given, only count free spots whose size is
        exactly `size` (not "fits" — an exact match on spot.size).
        """

        count = 0
        for spot in self.spots:
            if size and spot.size.value == size.value and not spot.is_occupied:
                count += 1
            elif not size:
                if not spot.is_occupied:
                    count += 1
    
        return count


        # raise NotImplementedError
