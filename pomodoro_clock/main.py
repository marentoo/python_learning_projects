from tkinter import *
import math
import pygame
import time

# ---------------------------- CONSTANTS ------------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
CHECKMARK = "✔"
REPS = 0
timer = None
clock_sound = "audio/audio.mp3"

# ---------------------------- TIMER RESET ---------------------------------- # 
def reset_timer():
    window.after_cancel(timer) ## stop counting
    canvas.itemconfig(timer_text, text="00:00")##reset title text to 00:00
    timer_label.config(text = "Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 50))##reset title label
    checkmark_label.config(text="") ## reset CHECKMARKS
    global REPS
    REPS = 0
    stop_audio()

# ---------------------------- TIMER MECHANISM ------------------------------ # 
def start_timer():
    stop_audio()
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN  * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:   #if 8th rep then - long break sec
        count_down(long_break_sec)
        timer_label.config(text="Long break",fg = "RED",bg = YELLOW, font=(FONT_NAME, 20))

    elif REPS %2 == 0:  #if 2nd 4th 6th 8th - short break sec
        count_down(short_break_sec)
        timer_label.config(text="break",fg = "RED",bg = YELLOW, font=(FONT_NAME, 50))

    else:   #if 1th 3th 5th 7th rep - work sec
        count_down(work_sec)
        timer_label.config(text = "Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 50))




# ---------------------------- COUNTDOWN MECHANISM -------------------------- #
def count_down(count):
    
    time_min = math.floor(count/60)
    time_sec = count % 60
    x = {0,1,2,3,4,5,6,7,8,9}
    if time_sec < 10:
        time_sec = f"0{time_sec}" #python dynamic typing!


    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS/2)
        for _ in range(work_session):
            marks += CHECKMARK
        checkmark_label.config(text=marks)

    if count > 0 and count < 6:
        play_audio()

## ---------------------------- Audio mechanism ----------------------------- #
pygame.mixer.init()
def play_audio():
    pygame.mixer.music.load(clock_sound)
    pygame.mixer.music.play(loops = 0)

def stop_audio():
    pygame.mixer.music.pause()


# ---------------------------- UI SETUP ------------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW, highlightthickness = 0)

#Canvas - image and text
canvas = Canvas(width = 200, height = 224)
tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(102, 112, image = tomato_img )
timer_text = canvas.create_text(102,130, text= "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

#Labels
timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column = 1, row = 0)

checkmark_label = Label(fg=GREEN)
checkmark_label.grid(column = 1, row = 4)

#Buttons
Start_button = Button(text = "Start", command = start_timer)
Start_button.grid(column = 0, row = 2)

Reset_button = Button(text = "Reset", command = reset_timer)
Reset_button.grid(column = 2, row = 2)




window.mainloop()