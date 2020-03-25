class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(val)

    def prepend(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            self.head.next = self.head
            self.head = Node(val)

    def insert(self, pos, val):
        current_node = self.head
        for i in range(0, pos):
            current_node = current_node.next

        current_node.next = current_node
        current_node = Node(val)

    def find(self, first, amt):
        current_node = self.head
        str = ""
        for i in range(0, first):
            current_node = current_node.next

        for i in range(0, amt):
            str += f"{current_node.val} "
            current_node = current_node.next

        return str

    def includes(self, value):
        current_node = self.head
        while current_node.next:
            if current_node.val == value:
                return True

        return False

    def count(self):

        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next

        return count

    def to_string(self):

        string = ""
        current_node = self.head
        while current_node:
            string += f" {current_node.val}"
            current_node = current_node.next

        return string

    def pop(self):
        node = self.head
        while node.next.next:
            node = node.next

        value = node.next.val
        node.next = None
        return value
