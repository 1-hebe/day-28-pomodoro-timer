from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier New"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_count)
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
        print("long rest")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
        print("short break")
    else:
        count_down(work_sec)
        timer.config(text="Working", fg=GREEN)
        print("working")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, timer_count
    count_min = math.floor(count/60) # calculate minutes remaining
    count_sec = count % 60 # calculate seconds remaining

    if count_sec < 10: # text formatting the seconds for a normal clock display
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_count = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row= 1, column= 1)

# Labels

timer = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg= GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

check_mark = Label(font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(row= 3, column=1)

# Buttons

start_button = Button(text="Start", font=(FONT_NAME, 20, "normal"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME,20,"normal"), command=reset_timer)
reset_button.grid(row=2, column=2)




window.mainloop()
