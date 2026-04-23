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

    def _pop_lru(self) -> None:
        lru = self.tail.prev
        self._remove_node(lru)
        return lru.value
    
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
    

