from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text = "Timer")
    check_mark_label.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps +=1
   
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
   
      
    if reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text= "Long Break",fg =RED)
    elif reps %2 ==0:
        count_down(short_break_sec)
        timer_label.config(text= "Short Break",fg =PINK)
    else:
        count_down(work_sec)
        timer_label.config(text= "Work",fg =GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = math.floor(count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    
        
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        startTimer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark +="✔"
            check_mark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx= 100, pady= 50, bg = YELLOW)
canvas = Canvas(width=205, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "./PomodoroApp/tomato.png" )
canvas.create_image(103,112,image =tomato_img )
timer_text = canvas.create_text(103,130, text = "00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer_label.grid(row=0,column= 1)

start_button= Button(text="Start",  highlightthickness=0,command=startTimer)
start_button.grid(row=2, column=0)
reset_button=  Button(text="Reset", highlightthickness=0,command=resetTimer,)
reset_button.grid(row=2, column = 3)
check_mark_label= Label( fg=GREEN, font=(FONT_NAME,10,"bold"), bg=YELLOW)
check_mark_label.grid(row=3, column=1)
window.mainloop()