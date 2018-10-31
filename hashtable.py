class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class HashTable():
    def __init__(self):
        self._size = 0
        self._capacity = 8
        self._data = [None] * self._capacity

    def __len__(self):
        return self._size

    def __setitem__(self, key, data):
        index = self._hash(key)
        node = None
        head = self._data[index]

        if head is not None:
            node = self._find_node(key, head)

        if node is not None:
            node.value = data
            return

        self._resize()

        if head is None:
            n = Node(key, data)

            self._data[index] = n
            self._size += 1

        else:
            self._append(key, data, head)

    def __getitem__(self, key):
        index = self._hash(key)

        head = self._data[index]
        node = self._find_node(key, head)
        if node is not None:
            return node.value

        return None

    def __delitem__(self, key):
        index = self._hash(key)
        head = self._data[index]

        if head is None:
            return

        if self._delete(key, head):
            self._size -= 1
            self._resize(increase=False)
            return

        return

    def __contains__(self, key):
        index = self._hash(key)

        head = self._data[index]

        return self._find_node(key, head) is not None

    def _hash(self, key):
        return key % self._capacity

    def _find_node(self, key, node):
        current = node

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return

    def _append(self, key, data, head):
        current = head

        while current.next is not None:
            current = current.next

        n = Node(key, data)

        current.next = n

        self._size += 1

    def _delete(self, key, head):
        if head.next is None and head.key == key:
            self._data[self._hash(key)] = head.next
            return True

        current = head.next
        prev = head

        while current.key != key:
            prev = current
            current = current.next

        if current.key == key:
            prev.next = current.next
            return True

        return False

    def _resize(self, increase=True):
        if increase and self._size / self._capacity >= 0.75:
            self._resize_up()
            return

        if not increase and self._capacity > 8 and self._size / self._capacity < 0.25:
            self._resize_down()

    def _resize_up(self):
        self._capacity *= 2
        self._rehash()

    def _resize_down(self):
        self._capacity //= 2
        self._rehash()

    def _rehash(self):
        old_data = self._data
        self._data = [None] * self._capacity
        self._size = 0

        for ll in old_data:
            current = ll

            while current is not None:
                self[ll.key] = ll.value
                current = current.next
