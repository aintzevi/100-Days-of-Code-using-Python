import turtle as t
import colorgram
from random import choice

pen = t.Turtle()

# We run the color extraction code only once, then just use the printed list of colors

# num_of_colors = 20
# colors = colorgram.extract("image.jpeg", num_of_colors)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(239, 238, 236), (238, 236, 237), (237, 241, 237), (26, 164, 108), (193, 81, 38), (237, 50, 161), (234, 86, 215), (227, 229, 237), (223, 176, 137), (143, 57, 108), (103, 219, 197), (21, 132, 57), (205, 30, 166), (213, 91, 74), (238, 49, 89), (142, 227, 208), (119, 139, 191), (5, 177, 185), (106, 198, 108), (137, 72, 29)]

t.colormode(255)
pen.speed("fastest")
pen.penup()
pen.hideturtle()

# Roughly positioning the pen to the bottom left side of the window
pen.setheading(220)
pen.forward(300)
pen.setheading(0)

num_of_rows_and_columns = 10

for dot_count in range(num_of_rows_and_columns):
    for j in range(num_of_rows_and_columns):
        pen.dot(20, choice(color_list))
        pen.fd(50)
    pen.sety(pen.ycor() + 50)
    pen.setx(pen.xcor() - 500)


screen = t.Screen()
screen.exitonclick()
