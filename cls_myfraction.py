# coding = utf-8
# cls_myfraction.py

from fractions import gcd

class myFraction(object):
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(r'%s/%s' %(self.num, self.den))
    
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        max_com_divisor = gcd(newnum, newden)
        
        if max_com_divisor == 1:
            return (r'%s/%s'%(newnum,newden))
        else:
            Newnum = newnum/max_com_divisor
            Newden = newden/max_com_divisor
            return (r'%s/%s'(Newnum,Newden))

myfraction = myFraction(3,5)
myf = myFraction(4,9)

myfraction.show()
myf.show()

data = myfraction + myf
print(data)