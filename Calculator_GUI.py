from tkinter import *

def add():
  
        a = int(txt1.get("1.0", "end-1c"))
        b = int(txt2.get("1.0", "end-1c"))
        result = a + b
        txt3.delete("1.0", END)
        txt3.insert("1.0", str(result))


def sub():
    
        a = int(txt1.get("1.0", "end-1c"))
        b = int(txt2.get("1.0", "end-1c"))
        result = a - b
        txt3.delete("1.0", END)
        txt3.insert("1.0", str(result))
    

def multi():
    
        a = int(txt1.get("1.0", "end-1c"))
        b = int(txt2.get("1.0", "end-1c"))
        result = a * b
        txt3.delete("1.0", END)
        txt3.insert("1.0", str(result))
   

def div():
   
        a = int(txt1.get("1.0", "end-1c"))
        b = int(txt2.get("1.0", "end-1c"))
        result = a / b
        txt3.delete("1.0", END)
        txt3.insert("1.0", str(result))
    

calculator = Tk()
calculator.title("GUI Calculator")
calculator.geometry("400x450")
calculator.resizable(False,False)

# Set background color for the main window
calculator.configure(bg="#808080")

lbl1 = Label(calculator, text="First Number :", bg="#e6e6e6")
lbl2 = Label(calculator, text="Second Number :", bg="#e6e6e6")
lbl3 = Label(calculator, text="Output :", bg="#e6e6e6")

btn1 = Button(calculator, text="Add", command=add, height=2, width=20, bg="#4caf50", fg="white")
btn2 = Button(calculator, text="Sub", command=sub, height=2, width=20, bg="#f44336", fg="white")
btn3 = Button(calculator, text="Multiply", command=multi, height=2, width=20, bg="#2196f3", fg="white")
btn4 = Button(calculator, text="Divide", command=div, height=2, width=20, bg="#ff9800", fg="white")

txt1 = Text(calculator, height=2, width=20)
txt2 = Text(calculator, height=2, width=20)
txt3 = Text(calculator, height=2, width=20)

footer = Label(calculator, text="2023 @ Waruna Liyanapathirana", font=("Arial", 10), bg="#C0C0C0", fg="black")
footer.pack(side=BOTTOM, fill=X)

lbl1.pack(pady=5)
txt1.pack(pady=5)
lbl2.pack(pady=5)
txt2.pack(pady=5)
btn1.pack(pady=5)
btn2.pack(pady=5)
btn3.pack(pady=5)
btn4.pack(pady=5)
lbl3.pack(pady=5)
txt3.pack(pady=5)

calculator.mainloop()
