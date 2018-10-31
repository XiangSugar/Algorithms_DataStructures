# coding = utf-8
# 2018-10-22   22:00

import turtle

def sierpinski(points, degree, myTurtle):
    colormpa = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormpa[degree], myTurtle)  # 该函数用于绘制并填充一个三角形
    if degree > 0:
        sierpinski([points[0], 
                    my_GetMid(points[0],points[1]),  # 返回两个点组成的线段的中点
                    my_GetMid(points[0],points[2])],
                    degree-1, myTurtle)
        sierpinski([points[1],
                    my_GetMid(points[0], points[1]),
                    my_GetMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                    my_GetMid(points[2], points[1]),
                    my_GetMid(points[0], points[2])],
                   degree-1, myTurtle)

def my_GetMid(pointa, pointb):
    pass
def drawTriangle(points, color, myTurtle):
    pass
    
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50], [0,100], [100,-50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

if __name__ == '__main__':
    main()
