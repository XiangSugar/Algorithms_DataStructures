# coding = utf-8
# 2018-10-19  21:20

'''利用Queue来简单判断回文词/数'''

from my_Deque import Deque

def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        firstch = chardeque.removeFront()
        lastch = chardeque.removeRear()
        if lastch != firstch:
            stillEqual = False
    return stillEqual

if __name__ == '__main__':
    print(palchecker("asyiriysa"))