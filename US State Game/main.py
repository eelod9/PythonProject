import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./US State Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("./US State Game/50_states.csv")
all_states = data.state.to_list()
game_is_on = True
guessed_states =[]


while(game_is_on):
   
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Next guess?").title()
    if answer_state == "Exit":
        break
    if(answer_state in all_states):
        print(f"{answer_state}  found")
        guessed_states.append(answer_state)
        #correct so print to screen
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(data[data.state == answer_state].x),int(data[data.state == answer_state].y))
        t.write(answer_state,align = "center", font="Courier")

need_to_learn = []
#states_to_learn.csv
for i in all_states:
    if i not in guessed_states:
        need_to_learn.append(i)

data1 = pandas.DataFrame(need_to_learn)

data1.to_csv("./US State Game/need_to_learn.csv")



print(need_to_learn)



 
           
'''
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''