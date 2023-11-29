from tkinter import *
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    lbl.config(text=current_time)
    clock.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

clock = Tk()
clock.title("Digital Clock")
clock.configure(bg="#FFFF00")
clock.geometry("636x160")
clock.resizable(False,False)
footer = Label(clock, text="2023 @ Waruna Liyanapathirana", font=("Arial", 10), bg="#C0C0C0", fg="black")
footer.pack(side=BOTTOM, fill=X)

lbl = Label(clock, font=("Times new roman", 90))
lbl.pack()

update_time()  # Initial call to start the clock updating

clock.mainloop()
