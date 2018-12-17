"""tile.py: Description of divide a rectangle.

__author__ = "陈新杨"
__pkuid__  = "1800011830"
__email__  = "1800011830@pku.edu.cn"
"""


import turtle
t = turtle.Pen()

def drawlist(list0):
    ###画出列表
    for i in list0:
        turtle.goto(i[0]*20,-i[1]*20)
        turtle.pendown()
        for j in range(4):
            turtle.forward(20)
            turtle.right(90)
        turtle.penup()

def drawbrick(brick):
    ###画出每一块砖
    turtle.pensize(5)
    spotbase = brick[0]
    long = max([spot[0] for spot in brick])-min([spot[0] for spot in brick])
    wide = max([spot[1] for spot in brick])-min([spot[1] for spot in brick])
    turtle.penup()
    turtle.goto(spotbase[0]*20,-spotbase[1]*20)
    turtle.pendown()
    for j in range(2):
        turtle.forward((long+1)*20)
        turtle.right(90)
        turtle.forward((wide+1)*20)
        turtle.right(90)


def standrec(a,b,i,j):
    ###竖着的矩形
    rec = []
    for k in range(a):
        for l in range(b):
            rec.append((i+l,j+k))
    return(rec)

def lierec(a,b,i,j):
    ###横着的矩形
    rec = []
    for k in range(b):
        for l in range(a):
            rec.append((i+l,j+k))
    return(rec)

def divide(a,b,m,n,list0,method = []):
    ###进行分割
    if (m*n)%(a*b) == 0:
        if len(method) == (m*n)/(a*b):
            nummethod = []
            for brick in method:
                numbrick = ()
                for spot in brick:
                    num = spot[0]+spot[1]*m
                    numbrick = numbrick + (num,)
                nummethod.append(numbrick)
            print(nummethod)
            global result
            result = result + [method]
            return()
        else:
            base = list0[0]
            x = base[0]
            y = base[1]
            for rec in [lierec,standrec]:
                if set(rec(a,b,x,y)) <= set(list0):
                    list1 = list0+[]
                    for i in rec(a,b,x,y):
                        list1.remove(i)
                    method1 = method + [rec(a,b,x,y)]
                    divide(a,b,m,n,list1,method1)
    else:
        return(False)

if __name__ == '__main__':
    result = []
    a = int(turtle.numinput("分割","请输入砖的长"))
    b = int(turtle.numinput("分割","请输入砖的宽"))
    m = int(turtle.numinput("分割","请输入墙的长"))
    n = int(turtle.numinput("分割","请输入墙的宽"))
    list0 = [(x,y) for x in range(m) for y in range(n)]
    divide(a,b,m,n,list0,method = [])
    x = len(result)
    y = int(turtle.numinput("Select Plan","Input number of 0-"+str(x-1)))
    Plan = result[y]
    drawlist(list0)
    for brick in Plan:
        drawbrick(brick)
