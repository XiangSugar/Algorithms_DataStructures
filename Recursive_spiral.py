# coding = utf-8
# 2018-10-22  09:41

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

def main():
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()

if __name__ == '__main__':
    main()