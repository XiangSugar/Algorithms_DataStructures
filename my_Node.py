# coding = utf-8
# 2018-10-20  09:18

'''节点类的实现'''

class my_Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None  # 用 None 来初始化对下一个节点的引用(节点接地)
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext

if __name__ == '__main__':
    temp = my_Node(93)
    print(temp)
    print(temp.getData())