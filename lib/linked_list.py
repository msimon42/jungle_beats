class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(val)

    def prepend(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            self.head.next = self.head
            self.head = Node(val)

    def insert(self, pos, val):
        last = self.head
        for i in range(0, pos):
            last = last.next

        last.next = last
        last = Node(val)

    def count(self):

        count = 0
        last = self.head
        while last:
            count += 1
            last = last.next

        return count

    def to_string(self):

        string = ""
        last = self.head
        while last:
            string += f" {last.val}"
            last = last.next

        return string
