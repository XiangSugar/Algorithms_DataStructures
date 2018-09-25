# coding = utf-8
# cls_myfraction.py

from fractions import gcd

class myFraction(object):
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    
    def show(self):
        print(r'%s/%s' %(self.num, self.den))
    
    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        max_com_divisor = gcd(newnum, newden)
        
        if max_com_divisor == 1:
            return (r'%s/%s' %(newnum,newden))
        else:
            simple_newnum = int(newnum/max_com_divisor)
            simple_newden = int(newden/max_com_divisor)
            return (r'%s/%s' %(simple_newnum,simple_newden))

myf_1 = myFraction(1,3)
myf_2 = myFraction(8,15)

myf_1.show()
print(myf_1)
myf_2.show()
print(myf_2)

data = myf_1 + myf_2
print(data)