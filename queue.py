class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        try:
            if isinstance(self.items, list):
                self.items.append(item)
        except ValueError:
            print("Invalid queue initialization")


    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def q_size(self):
        if not self.is_empty():
            return len(self.items)
        else:
            return 0