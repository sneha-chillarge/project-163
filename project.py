# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:22:35 2023

@author: Shree
"""

from tkinter import *
from tkinter import messagebox 
root =Tk()
root.title("report generator")
root.geometry("400x400")

question1_radiobutton = StringVar(value="0")
question2_radiobutton = StringVar(value="0")
question3_radiobutton = StringVar(value="0")

label_headache = Label(root,text="Do you have headache or a sorethroat?")
label_headache.pack()
question1_r1 = Radiobutton(root,text="yes", variable=question1_radiobutton , value="yes")
question1_r1.pack()
question1_r2 = Radiobutton(root,text="no", variable=question1_radiobutton , value="no")
question1_r2.pack()

label_fever = Label(root,text="Do you have high temperature?")
label_fever.pack()
question2_r1 = Radiobutton(root,text="yes", variable=question2_radiobutton , value="yes")
question2_r1.pack()
question2_r2 = Radiobutton(root,text="no", variable=question2_radiobutton , value="no")
question2_r2.pack()

label_eye_red = Label(root,text="Do you have eye redness?")
label_eye_red.pack()
question3_r1 = Radiobutton(root,text="yes", variable=question3_radiobutton , value="yes")
question3_r1.pack()
question3_r2 = Radiobutton(root,text="no", variable=question3_radiobutton , value="no")
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radiobutton.get()=="yes":
        score = score + 20
        print(score)
        
    if question2_radiobutton.get()=="yes":
        score = score + 20 
        print(score)
        
    if question3_radiobutton.get()=="yes":
        score = score + 20
        print(score)   
        
    if score <= 20:
        messagebox.showinfo("Report","You do not need to visit the doctor")
    elif score > 20 and score<=40:
        messagebox.showinfo("report","You might have to visit the doctor")
    else :
        messagebox.showinfo("Report","I strongly suggest you to visit the doctor")

btn_report = Button(root,text="Generate Report" , command=fever_score)
btn_report.pack()
root.mainloop()