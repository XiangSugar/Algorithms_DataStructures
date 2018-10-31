# coding = utf-8
# 2018-10-22   19:13

import turtle
from random import randrange

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20) #右转20°
        tree(branchLen - 15, t)
        t.left(40)  # 左转40°  对称
        tree(branchLen-15, t)
        t.right(20)  # 右转20°  回正
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(120)
    t.down()
    t.color("green")
    tree(105, t)
    myWin.exitonclick()

if __name__ == '__main__':
    main()
