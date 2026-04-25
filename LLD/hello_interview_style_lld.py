"""
Hello Interview-style LLD practice pack in Python.

For each problem, the file follows the same teaching spine:
1) Requirements and scope
2) Entities and relationships
3) Class design
4) Core implementation
5) Scenario-style tests

Problems included:
- Parking Lot
- Elevator System
- Movie Ticket Booking
- Rate Limiter
- LRU Cache
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
import heapq
import math
import time
import uuid


# ============================================================
# 1) PARKING LOT
# ============================================================


class VehicleType(Enum):
    MOTORCYCLE = auto()
    CAR = auto()
    TRUCK = auto()


class SpotType(Enum):
    MOTORCYCLE = auto()
    COMPACT = auto()
    LARGE = auto()


PARKING_FIT_ORDER = {
    VehicleType.MOTORCYCLE: [SpotType.MOTORCYCLE, SpotType.COMPACT, SpotType.LARGE],
    VehicleType.CAR: [SpotType.COMPACT, SpotType.LARGE],
    VehicleType.TRUCK: [SpotType.LARGE],
}


@dataclass
class Vehicle:
    plate: str
    vehicle_type: VehicleType


@dataclass
class ParkingSpot:
    spot_id: str
    spot_type: SpotType
    vehicle: Vehicle | None = None

    def is_free(self) -> bool:
        return self.vehicle is None

    def park(self, vehicle: Vehicle) -> None:
        if not self.is_free():
            raise ValueError(f"Spot {self.spot_id} is occupied")
        self.vehicle = vehicle

    def unpark(self) -> Vehicle:
        if self.vehicle is None:
            raise ValueError(f"Spot {self.spot_id} is already empty")
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle


@dataclass
class Ticket:
    ticket_id: str
    vehicle: Vehicle
    spot: ParkingSpot
    entry_time: int


class ParkingLot:
    """
    Orchestrator:
    - assigns a matching spot
    - issues a ticket
    - computes fee on exit
    """

    def __init__(self, spots: list[ParkingSpot], hourly_rates: dict[SpotType, int]):
        self.spots_by_type = defaultdict(list)
        for spot in spots:
            self.spots_by_type[spot.spot_type].append(spot)

        self.hourly_rates = hourly_rates
        self.active_tickets: dict[str, Ticket] = {}

    def park_vehicle(self, vehicle: Vehicle, entry_time: int | None = None) -> Ticket:
        if entry_time is None:
            entry_time = int(time.time())

        for spot_type in PARKING_FIT_ORDER[vehicle.vehicle_type]:
            for spot in self.spots_by_type[spot_type]:
                if spot.is_free():
                    spot.park(vehicle)
                    ticket = Ticket(
                        ticket_id=str(uuid.uuid4())[:8],
                        vehicle=vehicle,
                        spot=spot,
                        entry_time=entry_time,
                    )
                    self.active_tickets[ticket.ticket_id] = ticket
                    return ticket

        raise ValueError("No suitable spot available")

    def unpark_vehicle(self, ticket_id: str, exit_time: int | None = None) -> int:
        if ticket_id not in self.active_tickets:
            raise ValueError("Invalid ticket id")

        if exit_time is None:
            exit_time = int(time.time())

        ticket = self.active_tickets.pop(ticket_id)
        ticket.spot.unpark()

        elapsed_secs = max(0, exit_time - ticket.entry_time)
        billable_hours = max(1, math.ceil(elapsed_secs / 3600))
        rate = self.hourly_rates[ticket.spot.spot_type]
        return billable_hours * rate


# ============================================================
# 2) ELEVATOR SYSTEM
# ============================================================


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    IDLE = auto()


@dataclass
class ElevatorRequest:
    source: int
    destination: int

    @property
    def direction(self) -> Direction:
        if self.destination > self.source:
            return Direction.UP
        if self.destination < self.source:
            return Direction.DOWN
        return Direction.IDLE


class Elevator:
    """
    Elevator owns its own movement state.
    We separate pickup floors from drop-off floors.
    """

    def __init__(self, elevator_id: int, current_floor: int = 0):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.direction = Direction.IDLE

        self.pickup_up: list[int] = []
        self.pickup_down: list[int] = []  # max heap via negatives
        self.drop_up: list[int] = []
        self.drop_down: list[int] = []

        self.requests_by_pickup_floor: dict[int, list[ElevatorRequest]] = defaultdict(
            list
        )

    def queue_request(self, request: ElevatorRequest) -> None:
        if request.source == self.current_floor:
            self._pickup_passenger(request)
        elif request.source > self.current_floor:
            heapq.heappush(self.pickup_up, request.source)
            self.requests_by_pickup_floor[request.source].append(request)
        else:
            heapq.heappush(self.pickup_down, -request.source)
            self.requests_by_pickup_floor[request.source].append(request)

        if self.direction == Direction.IDLE:
            self.direction = (
                Direction.UP if request.source >= self.current_floor else Direction.DOWN
            )

    def _pickup_passenger(self, request: ElevatorRequest) -> None:
        if request.destination > self.current_floor:
            heapq.heappush(self.drop_up, request.destination)
        elif request.destination < self.current_floor:
            heapq.heappush(self.drop_down, -request.destination)

    def _process_current_floor(self) -> None:
        if self.current_floor in self.requests_by_pickup_floor:
            requests = self.requests_by_pickup_floor.pop(self.current_floor)
            for request in requests:
                self._pickup_passenger(request)

        while self.pickup_up and self.pickup_up[0] == self.current_floor:
            heapq.heappop(self.pickup_up)

        while self.pickup_down and -self.pickup_down[0] == self.current_floor:
            heapq.heappop(self.pickup_down)

        while self.drop_up and self.drop_up[0] == self.current_floor:
            heapq.heappop(self.drop_up)

        while self.drop_down and -self.drop_down[0] == self.current_floor:
            heapq.heappop(self.drop_down)

    def _has_up_work(self) -> bool:
        return bool(self.pickup_up or self.drop_up)

    def _has_down_work(self) -> bool:
        return bool(self.pickup_down or self.drop_down)

    def pending_stop_count(self) -> int:
        return (
            len(self.pickup_up)
            + len(self.pickup_down)
            + len(self.drop_up)
            + len(self.drop_down)
        )

    def step(self) -> None:
        self._process_current_floor()

        if self.direction == Direction.IDLE:
            if self._has_up_work():
                self.direction = Direction.UP
            elif self._has_down_work():
                self.direction = Direction.DOWN
            else:
                return

        if self.direction == Direction.UP:
            if self._has_up_work():
                self.current_floor += 1
            elif self._has_down_work():
                self.direction = Direction.DOWN
                self.current_floor -= 1
            else:
                self.direction = Direction.IDLE
                return

        elif self.direction == Direction.DOWN:
            if self._has_down_work():
                self.current_floor -= 1
            elif self._has_up_work():
                self.direction = Direction.UP
                self.current_floor += 1
            else:
                self.direction = Direction.IDLE
                return

        self._process_current_floor()

        if self.direction == Direction.UP and not self._has_up_work():
            self.direction = Direction.DOWN if self._has_down_work() else Direction.IDLE
        elif self.direction == Direction.DOWN and not self._has_down_work():
            self.direction = Direction.UP if self._has_up_work() else Direction.IDLE


class ElevatorController:
    """
    Controller is the orchestrator.
    It picks an elevator, then the elevator manages its own stops.
    """

    def __init__(self, elevator_count: int, initial_floors: list[int] | None = None):
        initial_floors = initial_floors or [0] * elevator_count
        self.elevators = [
            Elevator(i, current_floor=initial_floors[i]) for i in range(elevator_count)
        ]

    def request_elevator(self, source: int, destination: int) -> int:
        request = ElevatorRequest(source, destination)
        chosen = min(
            self.elevators,
            key=lambda e: (
                abs(e.current_floor - source),
                e.pending_stop_count(),
                e.elevator_id,
            ),
        )
        chosen.queue_request(request)
        return chosen.elevator_id

    def step_all(self) -> None:
        for elevator in self.elevators:
            elevator.step()


# ============================================================
# 3) MOVIE TICKET BOOKING
# ============================================================


class SeatStatus(Enum):
    AVAILABLE = auto()
    LOCKED = auto()
    BOOKED = auto()


@dataclass
class Seat:
    seat_id: str
    status: SeatStatus = SeatStatus.AVAILABLE
    locked_by: str | None = None
    lock_expiry: int | None = None


@dataclass
class Show:
    show_id: str
    movie_name: str
    seats: dict[str, Seat]


@dataclass
class Booking:
    booking_id: str
    user_id: str
    show_id: str
    seat_ids: list[str]
    is_confirmed: bool = False


class BookingService:
    """
    Orchestrator:
    - lock seats
    - confirm booking
    - release expired locks
    """

    def __init__(self, lock_timeout_secs: int = 300):
        self.lock_timeout_secs = lock_timeout_secs
        self.shows: dict[str, Show] = {}
        self.bookings: dict[str, Booking] = {}

    def add_show(self, show: Show) -> None:
        self.shows[show.show_id] = show

    def _cleanup_expired_locks(self, show: Show, now: int) -> None:
        for seat in show.seats.values():
            if (
                seat.status == SeatStatus.LOCKED
                and seat.lock_expiry is not None
                and seat.lock_expiry <= now
            ):
                seat.status = SeatStatus.AVAILABLE
                seat.locked_by = None
                seat.lock_expiry = None

    def lock_seats(
        self, user_id: str, show_id: str, seat_ids: list[str], now: int | None = None
    ) -> Booking:
        if now is None:
            now = int(time.time())

        show = self.shows[show_id]
        self._cleanup_expired_locks(show, now)

        for seat_id in seat_ids:
            seat = show.seats[seat_id]
            if seat.status != SeatStatus.AVAILABLE:
                raise ValueError(f"Seat {seat_id} is not available")

        for seat_id in seat_ids:
            seat = show.seats[seat_id]
            seat.status = SeatStatus.LOCKED
            seat.locked_by = user_id
            seat.lock_expiry = now + self.lock_timeout_secs

        booking = Booking(
            booking_id=str(uuid.uuid4())[:8],
            user_id=user_id,
            show_id=show_id,
            seat_ids=seat_ids,
            is_confirmed=False,
        )
        self.bookings[booking.booking_id] = booking
        return booking

    def confirm_booking(self, booking_id: str, now: int | None = None) -> Booking:
        if now is None:
            now = int(time.time())

        if booking_id not in self.bookings:
            raise ValueError("Invalid booking id")

        booking = self.bookings[booking_id]
        show = self.shows[booking.show_id]
        self._cleanup_expired_locks(show, now)

        for seat_id in booking.seat_ids:
            seat = show.seats[seat_id]
            if seat.status != SeatStatus.LOCKED or seat.locked_by != booking.user_id:
                raise ValueError("Seat lock expired or no longer owned by this user")

        for seat_id in booking.seat_ids:
            seat = show.seats[seat_id]
            seat.status = SeatStatus.BOOKED
            seat.locked_by = None
            seat.lock_expiry = None

        booking.is_confirmed = True
        return booking


# ============================================================
# 4) RATE LIMITER
# ============================================================


import time


class TokenBucket:
    def __init__(self, capacity, refill_rate_per_sec):
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.tokens = capacity
        self.last_refill_ts = time.time()

    def allow(self):
        now = time.time()

        # Add tokens based on time passed
        elapsed = now - self.last_refill_ts
        new_tokens = elapsed * self.refill_rate_per_sec
        self.tokens = min(self.capacity, self.tokens + new_tokens)

        # Update last refill time
        self.last_refill_ts = now

        # Allow request only if we have at least 1 token
        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False


class RateLimiter:
    def __init__(self, capacity, refill_rate_per_sec):
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.buckets = {}

    def allow_request(self, client_id):
        if client_id not in self.buckets:
            self.buckets[client_id] = TokenBucket(
                self.capacity,
                self.refill_rate_per_sec
            )

        bucket = self.buckets[client_id]
        return bucket.allow()


# ============================================================
# 5) LRU CACHE
# ============================================================


class _Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    """
    Hash map + doubly linked list.
    Head side is MRU. Tail side is LRU.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[int, _Node] = {}

        self.head = _Node()  # dummy head
        self.tail = _Node()  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node: _Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: _Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_front(self, node: _Node) -> None:
        self._remove_node(node)
        self._add_to_front(node)

    def _pop_lru(self) -> _Node:
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_front(node)
            return

        node = _Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.capacity:
            lru = self._pop_lru()
            del self.map[lru.key]


# ============================================================
# TESTS / VERIFICATION SCENARIOS
# ============================================================


def test_parking_lot() -> None:
    lot = ParkingLot(
        spots=[
            ParkingSpot("M1", SpotType.MOTORCYCLE),
            ParkingSpot("C1", SpotType.COMPACT),
            ParkingSpot("L1", SpotType.LARGE),
        ],
        hourly_rates={
            SpotType.MOTORCYCLE: 10,
            SpotType.COMPACT: 20,
            SpotType.LARGE: 30,
        },
    )

    car = Vehicle("KA01", VehicleType.CAR)
    ticket = lot.park_vehicle(car, entry_time=0)
    assert ticket.spot.spot_id == "C1"
    fee = lot.unpark_vehicle(ticket.ticket_id, exit_time=7200)  # 2 hours
    assert fee == 40


def test_elevator_system() -> None:
    controller = ElevatorController(elevator_count=2, initial_floors=[0, 10])
    chosen = controller.request_elevator(source=2, destination=7)
    assert chosen == 0

    for _ in range(10):
        controller.step_all()

    elevator = controller.elevators[0]
    assert elevator.current_floor >= 7
    assert elevator.pending_stop_count() == 0


def test_movie_booking() -> None:
    service = BookingService(lock_timeout_secs=60)
    show = Show(
        show_id="show-1",
        movie_name="Interstellar",
        seats={sid: Seat(sid) for sid in ["A1", "A2", "A3"]},
    )
    service.add_show(show)

    booking = service.lock_seats("user-1", "show-1", ["A1", "A2"], now=100)
    assert show.seats["A1"].status == SeatStatus.LOCKED
    confirmed = service.confirm_booking(booking.booking_id, now=120)
    assert confirmed.is_confirmed is True
    assert show.seats["A1"].status == SeatStatus.BOOKED
    assert show.seats["A2"].status == SeatStatus.BOOKED


def test_rate_limiter() -> None:
    limiter = RateLimiter(capacity=2, refill_rate_per_sec=1.0)

    assert limiter.allow_request("client-1", now=0.0) is True
    assert limiter.allow_request("client-1", now=0.0) is True
    assert limiter.allow_request("client-1", now=0.0) is False
    assert limiter.allow_request("client-1", now=1.0) is True


def test_lru_cache() -> None:
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10  # 1 becomes MRU
    cache.put(3, 30)  # evicts 2
    assert cache.get(2) == -1
    assert cache.get(3) == 30
    assert cache.get(1) == 10


def run_all_tests() -> None:
    tests = [
        test_parking_lot,
        test_elevator_system,
        test_movie_booking,
        test_rate_limiter,
        test_lru_cache,
    ]
    for test in tests:
        test()
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()
