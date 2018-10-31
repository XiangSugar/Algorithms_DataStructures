# coding = utf-8
# 2018-10-20  10:08

'''利用链表结构来实现无序列表'''
from my_Node import my_Node


class my_orderedList(object):
    def __init__(self):
        self.head = None    # head 其实是对链式存储结构的第一个节点的一个引用（本质上它是一个节点类型的值）

    def isEmpty(self):
        return self.head == None

    def add(self, newdata):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > newdata:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = my_Node(newdata)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def reMove(self, item):
        current = self.head
        previous = None
        found = None
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def showitems(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()


def main():
    UnorderedList = my_orderedList()
    print(UnorderedList.isEmpty())
    UnorderedList.add(43)
    UnorderedList.add(16)
    UnorderedList.add(6.99)
    UnorderedList.add(-56)
    UnorderedList.showitems()
    print(UnorderedList.size())
    print(UnorderedList.search(6.99))
    UnorderedList.reMove(6.99)
    UnorderedList.showitems()


if __name__ == '__main__':
    main()
