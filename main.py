""" import colorgram 

colors = colorgram.extract("image.jpg", 20)
print(colors)

my_colors = []

for i in range(0, len(colors)):
    red = colors[i].rgb[0]
    blue = colors[i].rgb[1]
    green = colors[i].rgb[2]
    color_tuple = (red, blue, green)
    my_colors.append(color_tuple)
    
print(my_colors) """

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61)]    

tim.penup()

def draw(dimension, space):
    tim.speed("fastest")
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    for i in range(dimension):
        for j in range(dimension):
            tim.dot(20, random.choice(color_list))
            tim.forward(space)   
        tim.backward(space*dimension)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)        


tim.hideturtle()
draw(10, 50) 


screen.exitonclick()    