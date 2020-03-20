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
