class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.head.next = Node(val)
            self.head = self.head.next
        self.len += 1

    def pop(self):
        if not self.tail:
            return
        self.tail = self.tail.next
        if self.tail == None:
            self.head = None
        self.len -= 1

    def __len__(self):
        return self.len


class HitCounter:
    def __init__(self):
        self.hits = Queue()

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.hits.tail != None and self.hits.tail.val <= timestamp - 300:
            v = self.hits.pop()
        return len(self.hits)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
