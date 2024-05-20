from tkinter import *

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x400")
window.configure(bg="#e6f7ff")  
def calculate_si():
    try:
        p = float(amount.get())
        r = float(ROI.get())
        t = float(time.get())
        si = (p * r * t) / 100
        si = round(si, 2)
        result_label.config(text="Simple Interest is: " + str(si))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

app_label = Label(window, text="Simple Interest CALCULATOR", fg="#003366", bg="#e6f7ff", font=("Helvetica Neue", 20, "bold"), bd=5)
app_label.place(x=30, y=20)

amount_label = Label(window, text="Principal Amount:", fg="#003366", bg="#e6f7ff", font=("Helvetica Neue", 12), bd=1)
amount_label.place(x=20, y=90)

amount = Entry(window, bd=2, width=22, font=("Helvetica Neue", 12))
amount.place(x=180, y=92)

ROI_label = Label(window, text="Rate of Interest:", fg="#003366", bg="#e6f7ff", font=("Helvetica Neue", 12))
ROI_label.place(x=20, y=140)

ROI = Entry(window, bd=2, width=15, font=("Helvetica Neue", 12))
ROI.place(x=180, y=142)

time_label = Label(window, text="Time Period (years):", fg="#003366", bg="#e6f7ff", font=("Helvetica Neue", 12))
time_label.place(x=20, y=185)

time = Entry(window, bd=2, width=15, font=("Helvetica Neue", 12))
time.place(x=180, y=187)

calculate_button = Button(window, text="CALCULATE", fg="white", bg="#66b3ff", bd=4, font=("Helvetica Neue", 12, "bold"), command=calculate_si)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window, text="Simple Interest", bg="#e6f7ff", fg="#003366", font=("Helvetica Neue", 12, "bold"))
result_frame.place(x=20, y=300, width=360, height=60)

result_label = Label(result_frame, text=" ", bg="#e6f7ff", fg="#003366", font=("Helvetica Neue", 12), width=33)
result_label.place(x=20, y=20)

window.mainloop()
