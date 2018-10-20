# coding = utf-8
# 2018-10-19  20:56
# 这里是自己的实现，collections 模块中有 deque 模块可直接使用

class Deque(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def qitems(self):
        return self.items

if __name__ == '__main__':
    d = Deque()
    print(d.isEmpty())
    d.addFront("dog")
    d.addRear(4)
    d.addFront("cat")
    d.addRear(True)

    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.qitems())
    print(d.removeRear())
    print(d.removeFront())

# print(d.qitems())