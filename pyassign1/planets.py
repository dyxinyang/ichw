"""planets.py:Description of how six planets go around the sun.

__author__ = "chen xinyang"
__pkuid__   ="1800011830"
__email__    ="1800011830@pku.edu.cn"
"""


 import turtle


 import math


 t = turtle.Pen()


 t.hideturtle()


 t.dot(5, 'yellow')


 t.speed(0)


 def step(turtle, x):


 for j in range(6):


		 t.pencolor(color[j])


		 t.penup()


		 t.goto(a[j]*math.cos(0.1*x-j*30)-j*20, b[j]*math.sin(0.1*x-j*30))


		 t.pendown()


	   t.dot(5,color[j])


		 t.undo()


		 t.goto(a[j]*math.cos(0.1*x+0.1-j*30)-j*20, b[j]*math.sin(0.1*x+0.1-j*30))


		 t.dot(5,color[j])


		 t.undo()

		
 color = ['blue', 'green', 'red', 'black', 'orange', 'sea green']


 a = [40, 100, 200, 300, 400, 500]


 b = [40, 80, 150, 250, 350, 450]


 for x in range(1000):


	   step(t, x)
