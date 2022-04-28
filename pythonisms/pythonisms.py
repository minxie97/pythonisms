class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __eq__(self, other):
        return list(self) == list(other)

    def __str__(self):
        output = ''
        for value in self:
            out += f'[ {value } ] -> '
        out += 'None'
        return output


class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_
