class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.__str__())
            current = current.next

        return "->".join(values)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index > self.length - 1:
            raise Exception
        current = self.head

        for i in range(index):
            current = current.next

        return current.value

    def append(self, value):
        self.length += 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def reverse(self):
        if self.head is None:
            return

        if self.head.next is None:
            return

        prev = self.head
        curr = self.head.next
        prev.next = None

        while curr is not None:
            temp = curr.next

            curr.next = prev
            prev = curr
            curr = temp

        self.head = prev

        return self

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return self

        prev = self.head
        curr = self.head

        while curr is not None:
            if curr.value == value:
                self._delete_next(prev)
                self.length -= 1
                return self

            prev = curr
            curr = curr.next

        return self

    def _delete_next(self, node):
        node.next = node.next.next
