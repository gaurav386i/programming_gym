import threading


class _Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.next: "_Node | None" = None
        self.prev: "_Node | None" = None


class LRUCache:
    """
    hashmap + doubly linked list

    head side = MRU
    tail side = LRU
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap: dict[int, _Node] = {}

        self.head = _Node(-1, -1)
        self.tail = _Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        # minimal thread safety
        self.lock = threading.RLock()

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
        with self.lock:
            if key not in self.hmap:
                return -1

            node = self.hmap[key]
            self._move_to_front(node)

            return node.value

    def put(self, key: int, value: int) -> None:
        with self.lock:
            if key in self.hmap:
                node = self.hmap[key]
                node.value = value

                self._move_to_front(node)
                return

            node = _Node(key, value)

            self.hmap[key] = node
            self._add_to_front(node)

            if len(self.hmap) > self.capacity:
                lru = self._pop_lru()
                del self.hmap[lru.key]