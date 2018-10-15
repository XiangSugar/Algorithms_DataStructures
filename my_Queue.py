# coding = utf-8
# 2018年10月15日 21点52分
# 借助 list 来帮助建立队列的新类

class my_Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q = my_Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

print(q.size())