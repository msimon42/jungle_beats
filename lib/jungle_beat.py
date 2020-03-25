class JungleBeat:
    def __init__(self):
        self.list = LinkedList()

    def append(self, data):
        data_list = data.split(' ')

        for item in data_list:
            self.list.append(item)

        return data    
