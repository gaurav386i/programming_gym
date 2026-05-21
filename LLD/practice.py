import threading
import queue
import time


class _Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    """
    Hashmap + doubly linked list
    Head side is MRU. Tail side is LRU
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict[int, _Node] = {}

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
    

### Producer Consumer ######

NUM_OF_PRODUCERS = 5
NUM_OF_CONSUMERS = 3
NUM_OF_ITEM_PER_PRODUCER = 10

q = queue.Queue(maxsize=20)

lock = threading.Lock()

consumed_item = []


def producer(producer_id: int) -> None:
    for i in range(NUM_OF_ITEM_PER_PRODUCER):
        item = (producer_id, i)
        q.put(item)  # bloks if queue is full


def consumer() -> None:
    while True:
        item = q.get()  # blocks if q is empty

        if item is None:
            q.task_done()
            break
        # use locking to update a shared resource
        with lock:
            consumed_item.append(item)
        q.task_done()


producers = [
    threading.Thread(target=producer, args=(i,))
    for i in range(NUM_OF_PRODUCERS)
]

consumers = [
    threading.Thread(target=consumer)
    for _ in range(NUM_OF_CONSUMERS)
]

for c in consumers:
    c.start()

for p in producers:
    p.start()

for p in producers:
    p.join()

for _ in range(NUM_OF_CONSUMERS):
    q.put(None)

q.join()  # wait until all work is done

for c in consumers:
    c.join()

# print(len(consumed_item) == NUM_OF_PRODUCERS * NUM_OF_ITEM_PER_PRODUCER)

#=====Rate Limiter =============#
class TokenBucket:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate_per_sec = refill_rate_per_sec
        self.tokens = capacity
        self.last_refill_ts = time.time()

    def allow(self):
        now = time.time()
        elapsed_time = now - self.last_refill_ts
        new_tokens = elapsed_time * self.refill_rate_per_sec

        self.tokens = min(self.capacity, self.tokens + new_tokens)

        self.last_refill_ts = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    

class RateLimiter:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
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
    



#####=========Vending Machine =================#########

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_money(self, amount: float):
        pass

    @abstractmethod
    def select_item(self, item_id: str):
        pass

    @abstractmethod
    def dispense(self):
        pass

    @abstractmethod
    def refund(self):
        pass



class IdleState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_money(self, amount):
        self.machine.balance += amount
        print(f"Money inserted: ${amount}. Balance: ${self.machine.balance}")
        self.machine.set_state(self.machine.has_money_state)

    def select_item(self, item_id):
        print("Insert money first.")

    def dispense(self):
        print("Insert money first.")

    def refund(self):
        print("No money to refund.")

class HasMoneyState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_money(self, amount):
        self.machine.balance += amount
        print(f"Additional money: ${amount}. New balance: ${self.machine.balance}")

    def select_item(self, item_id):
        item = self.machine.inventory.get(item_id)
        if not item or item['count'] == 0:
            print("Out of stock!")
        elif self.machine.balance >= item['price']:
            self.machine.selected_item = item_id
            print(f"Item {item_id} selected.")
            self.machine.set_state(self.machine.dispensing_state)
        else:
            print(f"Insufficient funds. Need ${item['price'] - self.machine.balance} more.")

    def dispense(self):
        print("Select an item first.")

    def refund(self):
        print(f"Returning ${self.machine.balance}")
        self.machine.balance = 0
        self.machine.set_state(self.machine.idle_state)

class DispensingState(State):
    def __init__(self, machine):
        self.machine = machine

    def insert_money(self, amount):
        print("Wait, dispensing in progress...")

    def select_item(self, item_id):
        print("Already dispensing an item.")

    def dispense(self):
        item_id = self.machine.selected_item
        item = self.machine.inventory[item_id]
        
        # Logic for dispensing
        item['count'] -= 1
        change = self.machine.balance - item['price']
        self.machine.balance = 0
        self.machine.selected_item = None
        
        print(f"Dispensing {item_id}. Change returned: ${change:.2f}")
        self.machine.set_state(self.machine.idle_state)

    def refund(self):
        print("Cannot refund during dispensing.")


class VendingMachine:
    def __init__(self):
        self.inventory = {"A1": {"price": 1.5, "count": 5}, "B1": {"price": 2.0, "count": 1}}
        self.balance = 0.0
        self.selected_item = None
        
        # Initialize States
        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispensing_state = DispensingState(self)
        
        self.current_state = self.idle_state

    def set_state(self, state: State):
        self.current_state = state

    # Delegation methods
    def insert_money(self, amount): self.current_state.insert_money(amount)
    def select_item(self, item_id): self.current_state.select_item(item_id)
    def dispense(self): self.current_state.dispense()
    def refund(self): self.current_state.refund()
    



def test_rate_limiter() -> None:
    limiter = RateLimiter(capacity=2, refill_rate_per_sec=1.0)

    assert limiter.allow_request("client-1") is True
    assert limiter.allow_request("client-1") is True
    assert limiter.allow_request("client-1") is False

    time.sleep(1.01)
    assert limiter.allow_request("client-1") is True

def run_all_tests() -> None:
    tests = [ 
        test_rate_limiter,
    ]
    for test in tests:
        test()
    print("All tests passed.")


if __name__ == "__main__":
    run_all_tests()
