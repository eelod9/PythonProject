import colorgram as c
import turtle as t
import random
t.colormode(255)
'''
colors = c.extract("image.jpg", 30)
#print(colors)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''

color_list = [ (234, 247, 236), (202, 167, 135), (236, 243, 249), (144, 52, 97), (163, 167, 41), (237, 71, 121), (237, 83, 60), (17, 140, 65), (240, 220, 69), (225, 119, 162), (10, 142, 176), (65, 198, 218), 
(23, 169, 129), (158, 59, 52), (130, 187, 160), (109, 41, 85), (247, 232, 1), (34, 185, 201), (232, 165, 190), (247, 167, 152), (142, 214, 224), (146, 215, 190), (80, 37, 73), (5, 114, 35), (133, 38, 32)]
def randomize_color():
    return random.choice(color_list)


timmy = t.Turtle()
timmy.penup()
timmy.hideturtle()
#timmy.dot(20, random_color)
timmy.shape("circle")
starting_position = int(-400)

while(starting_position < 100):
    timmy.setposition(-400,starting_position)
    for i in range(10): 
        random_color = randomize_color()
        timmy.color(random_color)
        timmy.dot(20, random_color) 
        timmy.stamp()
        timmy.fd(50)
    starting_position += 50










screen = t.Screen()
screen.exitonclick()

   # for i in range(10): 
        



