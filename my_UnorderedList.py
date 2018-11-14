# coding = utf-8
# 2018-10-20  10:08

'''利用链表结构来实现无序列表'''
from my_Node import my_Node

class my_UnorderedList(object):
    def __init__(self):
        self.head = None    # head 其实是对链式存储结构的第一个节点的一个引用（注意：它到底是不是一个节点类型的值？？？？没太想清楚）
    def isEmpty(self):
        return self.head == None
    def add(self, newdata):
        temp = my_Node(newdata)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count   = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
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
        if previous == None:  # 表明第一项正好是要删除的值，则只需要把 head 往后移动一下即可，也没有前一个节点的说法了，因此不用管 previous
            self.head = current.getNext()
        else:                 # 表明删除的值不是第一项，则需要将 previous 指向的节点的对下一个节点的引用往后挪动一下
            previous.setNext(current.getNext())
    def showitems(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

def main():
    UnorderedList = my_UnorderedList()
    print(UnorderedList.isEmpty())
    UnorderedList.add(43)
    UnorderedList.add("Dog")
    UnorderedList.add(6.99)
    UnorderedList.add('jlasd')
    UnorderedList.showitems()
    print(UnorderedList.size())
    print(UnorderedList.search("Dog"))
    UnorderedList.reMove(6.99)
    UnorderedList.showitems()
    
if __name__ == '__main__':
    main()
    

    
