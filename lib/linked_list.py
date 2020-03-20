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

                
