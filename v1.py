from tkinter import *
from tkinter import messagebox

def submit():
    myFile = open(r"School\Assignments\Quiz\quiz.txt", "a")
    myFile.write(q.get()+",,"+a.get()+",,"+b.get()+",,"+c.get()+",,"+d.get(), "\n")
    myFile.close()
    messagebox.INFO(Text="The question has been saved succesfully")
    q.set("")
    a.set("")
    b.set("")
    c.set("")
    d.set("")

root = Tk()
root.geometry("800x130")
q, a, b, c, d = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
Label(root, text="Question").grid(row=0, column=0)
Entry(textvariable=q, width=117).grid(row=0, column=1)
Label(root, text="Correct answer").grid(row=1, column=0)
Entry(textvariable=a, width=117).grid(row=1, column=1)
Label(root, text="Wrong answer").grid(row=2, column=0)
Entry(textvariable=b, width=117).grid(row=2, column=1)
Label(root, text="Wrong answer").grid(row=3, column=0)
Entry(textvariable=c, width=117).grid(row=3, column=1)
Label(root, text="Wrong answer").grid(row=4, column=0)
Entry(textvariable=d, width=117).grid(row=4, column=1)
Button(root, text="Sumbit", command=submit).grid(row=5, column=0)
mainloop()