import queue
import threading

NUM_OF_PRODUCER = 5
NUM_OF_CONSUMER = 3
NUM_OF_ITEM_PER_PRODUCER = 10

q = queue.Queue(maxsize=20)

lock = threading.Lock()

consumed_items = []

def producer(producer_id: str) -> None:
    for i in range(NUM_OF_CONSUMER):
        item = (producer_id, i)
        q.put(item) # blocked if queue is full

def consumer() -> None:
    while True:
        item = q.get() # blocked if queue is empty 
        
        if item is None:
            q.task_done()
            break

        with lock:
            consumed_items.append(item)
        q.task_done()

producers = [
    threading.Thread(target=producer, args=(i,)) 
    for i in range(NUM_OF_PRODUCER)
]

consumers = [
    threading.Thread(target=consumer)
    for i in range(NUM_OF_CONSUMER)
]


for c in consumers:
    c.start()

for p in producers:
    p.start()


for p in producers:
    p.join()

for _ in range(NUM_OF_CONSUMER):
    q.put(None)



q.join()

for c in consumers:
    c.join()


### +++++++++++++++++++++++++++++++=###########

#### +++++++++++++++++++++++++++++++#############
import queue
import threading
from abc import ABC, abstractmethod
from typing import Any, List, Tuple

# --- Interfaces (DIP & OCP) ---

class DataPipeline(ABC):
    """Abstract interface for the messaging/data exchange channel."""
    @abstractmethod
    def put(self, item: Any) -> None:
        pass

    @abstractmethod
    def get(self) -> Any:
        pass

    @abstractmethod
    def task_done(self) -> None:
        pass

    @abstractmethod
    def join(self) -> None:
        pass


class ResultRepository(ABC):
    """Abstract interface for storing consumed/processed items safely."""
    @abstractmethod
    def save(self, item: Any) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        pass


# --- Concrete Implementations (SRP) ---

class ThreadSafeQueuePipeline(DataPipeline):
    """Capsule for thread-safe queue operations using standard queue.Queue."""
    def __init__(self, maxsize: int = 20):
        self._queue = queue.Queue(maxsize=maxsize)

    def put(self, item: Any) -> None:
        self._queue.put(item)

    def get(self) -> Any:
        return self._queue.get()

    def task_done(self) -> None:
        self._queue.task_done()

    def join(self) -> None:
        self._queue.join()


class ThreadSafeListRepository(ResultRepository):
    """Thread-safe storage mechanism wrapping an internal collection."""
    def __init__(self):
        self._lock = threading.Lock()
        self._storage = []

    def save(self, item: Any) -> None:
        with self._lock:
            self._storage.append(item)

    def get_all(self) -> List[Any]:
        with self._lock:
            return list(self._storage)


class ProducerWorker:
    """Responsible solely for generating items and loading them into a pipeline."""
    def __init__(self, producer_id: int, pipeline: DataPipeline, items_to_produce: int):
        self._id = f"Producer-{producer_id}"
        self._pipeline = pipeline
        self._items_to_produce = items_to_produce

    def run(self) -> None:
        for i in range(self._items_to_produce):
            item = (self._id, i)
            self._pipeline.put(item)


class ConsumerWorker:
    """Responsible solely for fetching items and saving them via a repository."""
    def __init__(self, pipeline: DataPipeline, repository: ResultRepository, poison_pill: Any = None):
        self._pipeline = pipeline
        self._repository = repository
        self._poison_pill = poison_pill

    def run(self) -> None:
        while True:
            item = self._pipeline.get()
            
            if item == self._poison_pill:
                self._pipeline.task_done()
                break

            self._repository.save(item)
            self._pipeline.task_done()


# --- Orchestrator/Coordinator ---

class ProducerConsumerEngine:
    """Handles thread lifecycle management, configuration, and orchestration."""
    POISON_PILL = None

    def __init__(self, num_producers: int, num_consumers: int, items_per_producer: int):
        self._num_producers = num_producers
        self._num_consumers = num_consumers
        self._items_per_producer = items_per_producer
        
        # Injecting dependencies
        self._pipeline = ThreadSafeQueuePipeline(maxsize=20)
        self._repository = ThreadSafeListRepository()

    def start(self) -> List[Any]:
        # Initialize Workers
        producers = [
            ProducerWorker(i, self._pipeline, self._items_per_producer)
            for i in range(self._num_producers)
        ]
        consumers = [
            ConsumerWorker(self._pipeline, self._repository, self.POISON_PILL)
            for _ in range(self._num_consumers)
        ]

        # Bind to native Threads
        producer_threads = [threading.Thread(target=p.run) for p in producers]
        consumer_threads = [threading.Thread(target=c.run) for c in consumers]

        # Execution Lifecycle
        for t in consumer_threads:
            t.start()
        for t in producer_threads:
            t.start()

        # Await producer completion
        for t in producer_threads:
            t.join()

        # Signal termination to consumers (Poison Pill Strategy)
        for _ in range(self._num_consumers):
            self._pipeline.put(self.POISON_PILL)

        # Synchronize queue and clean up consumers
        self._pipeline.join()
        for t in consumer_threads:
            t.join()

        return self._repository.get_all()


# --- Driver Code ---
if __name__ == "__main__":
    CONFIG = {
        "NUM_OF_PRODUCER": 5,
        "NUM_OF_CONSUMER": 3,
        "NUM_OF_ITEM_PER_PRODUCER": 10
    }

    engine = ProducerConsumerEngine(
        num_producers=CONFIG["NUM_OF_PRODUCER"],
        num_consumers=CONFIG["NUM_OF_CONSUMER"],
        items_per_producer=CONFIG["NUM_OF_ITEM_PER_PRODUCER"]
    )
    
    results = engine.start()
    print(f"Execution complete. Total items processed safely: {len(results)}")