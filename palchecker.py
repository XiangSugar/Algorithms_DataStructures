# coding = utf-8
# 2018-10-19  21:20

'''利用Dque来简单判断回文词/数'''

# 先将需要判断的内容（字符串格式）用双端队列存储起来
# 依次取出首尾的两个字符进行比较，看是否相等，直到结束

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
