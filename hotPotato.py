# coding  = utf-8
# 2018-10-16  08:49

'''Simulating hot potato problems with queues'''

# from pythonds.basicqueue 
from queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.put(name)

    while(simqueue.qsize() > 1):
        for i in range(num):
            simqueue.put(simqueue.get())
        simqueue.get()
    
    return simqueue.get()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', "Kant", 'Brad'], 7))


