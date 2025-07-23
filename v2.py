from tkinter import *
from tkinter import messagebox
import time, random

def getQ():
    with open("quiz.txt", "r") as f:
        lines = [line.strip().split(',,') for line in f]
        f.close()
    length = len(lines)
    order = random.sample(range(length), 10)
    print(order)
    q = []
    a = []
    b = []
    c = []
    d = []
    e = []
    for item in order:
        q.append(lines[item][0])
        order2 = random.sample(range(1, 5), 4)
        a.append(lines[item][order2[0]])
        b.append(lines[item][order2[1]])
        c.append(lines[item][order2[2]])
        d.append(lines[item][order2[3]])
        e.append(order2.index(1))
    return([q, a, b, c, d, e])

def getHigh():
    with open("scores.txt", "r") as f:
        scores = [line.strip().split(',,') for line in f]
        f.close()
    high = []
    for item in scores:
        item[1] = int(item[1])
        if len(high) == 0:
            high.append(item)
        elif len(high) == 1:
            if item[1] > high[0][1]:
                temp = high[0]
                high[0] = item
                high.append(temp)
            else:
                high.append(item)
        elif len(high) == 2:
            if item[1] > high[0][1]:
                temp = high[1]
                high[1] = high[0]
                high[0] = item
                high.append(temp)
            elif item[1] > high[1][1]:
                temp = high[1]
                high[1] = item
                high.append(temp)
            else:
                high.append(item)
        elif len(high) == 3:
            if item[1] > high[0][1]:
                high[2] = high[1]
                high[1] = high[0]
                high[0] = item
            elif item[1] > high[1][1]:
                high[2] = high[1]
                high[1] = item
            elif item[1] > high[2][1]:
                high[2] = item
    return(high)

def end():
    global root, score, q, a, b, c, d, e, question, data, startTime
    endTime = time.time()
    timeTaken = endTime - startTime
    qScore = int(100-timeTaken*5)
    if qScore > 0 and data.get() == e[question]:
        score = score + qScore
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x500")
    data = StringVar()
    Label(text=" ").grid(row=0, column=0)
    Label(text="Game End", font=("Times", "24", "bold italic"), width=40, height=2).grid(row=1, column=0, columnspan=2)
    Label(text="Enter Name", font=("Times", "20")).grid(row=2, column=0)
    Entry(textvariable=data, font=("Times", "20")).grid(row=2, column=1)
    Button(text="Back to title", bg="powderblue", font=("Times", "24", "bold italic"), width=20, height=2, command=loadStart2).grid(row=3, column=0)
    Button(text="Save and Back to title", bg="powderblue", font=("Times", "24", "bold italic"), width=20, height=2, command=loadStart3).grid(row=3, column=1)
    Label(text="Your Score: {0}".format(score), font=("Times", "24", "bold italic"), width=40, height=2).grid(row=4, column=0, columnspan=2)

def submit():
    global root, score, q, a, b, c, d, e, question, data, startTime
    for widget in root.winfo_children():
        widget.destroy()
    endTime = time.time()
    timeTaken = endTime - startTime
    qScore = int(100-timeTaken*5)
    if qScore > 0 and data.get() == e[question]:
        score = score + qScore
    question = question + 1
    data = IntVar(value=0)
    root.geometry("800x500")
    Label(text=" ").grid(row=0, column=0)
    Label(text="Quiz", font=("Times", "24", "bold italic"), width=40, height=2).grid(row=1, column=0, columnspan=2)
    Label(text="Score: {0}".format(score), font=("Times", "20"), fg="red").grid(row=2, column=0)
    Label(text="Question: {0}".format(question+1), font=("Times", "20"), fg="red").grid(row=2, column=1)
    Label(text=q[question], font=("Times", "20"), wraplength=750, height=3).grid(row=3, column=0, columnspan=2)
    Radiobutton(root, text=a[question], variable=data, value=0, font=("Times", "13")).grid(row=4, column=0)
    Radiobutton(root, text=b[question], variable=data, value=1, font=("Times", "13")).grid(row=5, column=0)
    Radiobutton(root, text=c[question], variable=data, value=2, font=("Times", "13")).grid(row=6, column=0)
    Radiobutton(root, text=d[question], variable=data, value=3, font=("Times", "13")).grid(row=7, column=0)
    if question == 9:
        Button(text="End", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=2, command=end).grid(row=8, column=0, columnspan=2)
    else:
        Button(text="Submit", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=2, command=submit).grid(row=8, column=0, columnspan=2)
    startTime = time.time()
    root.mainloop()

def start():
    global root, score, q, a, b, c, d, e, question, data, startTime
    score = 0
    question = 0
    q, a, b, c, d, e = getQ()
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x500")
    data = IntVar(value=0)
    Label(text=" ").grid(row=0, column=0)
    Label(text="Quiz", font=("Times", "24", "bold italic"), width=40, height=2).grid(row=1, column=0, columnspan=2)
    Label(text="Score: 0", font=("Times", "20"), fg="red").grid(row=2, column=0)
    Label(text="Question: 1", font=("Times", "20"), fg="red").grid(row=2, column=1)
    Label(text=q[0], font=("Times", "20"), wraplength=750, height=3).grid(row=3, column=0, columnspan=2)
    Radiobutton(root, text=a[0], variable=data, value=0, font=("Times", "13")).grid(row=4, column=0)
    Radiobutton(root, text=b[0], variable=data, value=1, font=("Times", "13")).grid(row=5, column=0)
    Radiobutton(root, text=c[0], variable=data, value=2, font=("Times", "13")).grid(row=6, column=0)
    Radiobutton(root, text=d[0], variable=data, value=3, font=("Times", "13")).grid(row=7, column=0)
    Button(text="Submit", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=2, command=submit).grid(row=8, column=0, columnspan=2)
    startTime = time.time()
    root.mainloop()

def loadStart():
    global root
    high = getHigh()
    root = Tk()
    root.geometry("800x450")
    Label(text=" ").grid(row=0, column=0)
    Button(text="Start", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=3, command=start).grid(row=1, column=0, columnspan=2, sticky="n")
    Label(text=" ", height=5).grid(row=2, column=0)
    Label(text="Highscores", font=("Times", "24", "bold italic")).grid(row=3, column=0, columnspan=2)
    Label(text=high[0][0], font=("Times", "20"), bg="gold", width=26).grid(row=4, column=0, sticky="nw")
    Label(text=high[0][1], font=("Times", "20"), bg="gold", width=27).grid(row=4, column=1, sticky="nw")
    Label(text=high[1][0], font=("Times", "20"), bg="silver", width=26).grid(row=5, column=0, sticky="nw")
    Label(text=high[1][1], font=("Times", "20"), bg="silver", width=27).grid(row=5, column=1, sticky="nw")
    Label(text=high[2][0], font=("Times", "20"), bg="goldenrod", width=26).grid(row=6, column=0, sticky="nw")
    Label(text=high[2][1], font=("Times", "20"), bg="goldenrod", width=27).grid(row=6, column=1, sticky="nw")
    messagebox.showinfo(title="INFO", message="When you press the start button you have 20 seconds to get the answer correct and submit.\nThe longer you take the less points you get\nThere are 10 questions worth 100 points each.\nBonne chance!")
    root.mainloop()

def loadStart2():
    global root
    high = getHigh()
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x450")
    Label(text=" ").grid(row=0, column=0)
    Button(text="Start", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=3, command=start).grid(row=1, column=0, columnspan=2, sticky="n")
    Label(text=" ", height=5).grid(row=2, column=0)
    Label(text="Highscores", font=("Times", "24", "bold italic")).grid(row=3, column=0, columnspan=2)
    Label(text=high[0][0], font=("Times", "20"), bg="gold", width=26).grid(row=4, column=0, sticky="nw")
    Label(text=high[0][1], font=("Times", "20"), bg="gold", width=27).grid(row=4, column=1, sticky="nw")
    Label(text=high[1][0], font=("Times", "20"), bg="silver", width=26).grid(row=5, column=0, sticky="nw")
    Label(text=high[1][1], font=("Times", "20"), bg="silver", width=27).grid(row=5, column=1, sticky="nw")
    Label(text=high[2][0], font=("Times", "20"), bg="goldenrod", width=26).grid(row=6, column=0, sticky="nw")
    Label(text=high[2][1], font=("Times", "20"), bg="goldenrod", width=27).grid(row=6, column=1, sticky="nw")
    root.mainloop()

def loadStart3():
    global root
    f = open("School\Assignments\Quiz\scores.txt", "a")
    f.write("\n{0},,{1}".format(data.get(), score))
    f.close()
    high = getHigh()
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry("800x450")
    Label(text=" ").grid(row=0, column=0)
    Button(text="Start", bg="powderblue", font=("Times", "24", "bold italic"), width=40, height=3, command=start).grid(row=1, column=0, columnspan=2, sticky="n")
    Label(text=" ", height=5).grid(row=2, column=0)
    Label(text="Highscores", font=("Times", "24", "bold italic")).grid(row=3, column=0, columnspan=2)
    Label(text=high[0][0], font=("Times", "20"), bg="gold", width=26).grid(row=4, column=0, sticky="nw")
    Label(text=high[0][1], font=("Times", "20"), bg="gold", width=27).grid(row=4, column=1, sticky="nw")
    Label(text=high[1][0], font=("Times", "20"), bg="silver", width=26).grid(row=5, column=0, sticky="nw")
    Label(text=high[1][1], font=("Times", "20"), bg="silver", width=27).grid(row=5, column=1, sticky="nw")
    Label(text=high[2][0], font=("Times", "20"), bg="goldenrod", width=26).grid(row=6, column=0, sticky="nw")
    Label(text=high[2][1], font=("Times", "20"), bg="goldenrod", width=27).grid(row=6, column=1, sticky="nw")
    root.mainloop()

loadStart()