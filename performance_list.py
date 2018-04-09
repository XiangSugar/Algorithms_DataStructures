# coding : utf-8

import timeit
from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = Timer('test1()', 'from __main__ import test1')
print('concat ', t1.timeit(number=1000), 'milliseconds')
t2 = Timer('test2()', 'from __main__ import test2')
print('append ', t2.timeit(number=1000), 'milliseconds')
t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension ', t3.timeit(number=1000), 'milliseconds')
t4 = Timer('test4()', 'from __main__ import test4')
print('list ', t4.timeit(number=1000), 'milliseconds')



# -----------------------The result--------------------------
# concat  2.1304368 milliseconds
# append  0.17162760000000032 milliseconds
# comprehension  0.02869020000000022 milliseconds
# list  0.01205949999999989 milliseconds
# -----------------------------------------------------------