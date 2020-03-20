class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head is None:
            self.head = val
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = val

    def count(self):
        if self.head is None:
            return 0
        else:
            count = 1
            last = self.head
            while last.next:
                count += 1

            return count
