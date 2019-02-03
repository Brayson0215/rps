from tkinter import*
global operator
operator=''
def caseClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def caseClearTextDisplay():
    global operator
    operator=""
    text_input.set("")
def caseEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator = ""
root=Tk()
root.title("BRAYSON")
text_Input=StringVar()
txtDisplay=Entry(root,font=('arial',15,'bold'),textvariable=text_Input,bd=20,insertwidth=5,bg="gray",justify='right').grid(columnspan=4)
button7=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(7), text="7",bd=10).grid(row=1, column=0)
button8=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(8),text="8",bd=10).grid(row=1, column=1)
button9=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(9),text="9",bd=10).grid(row=1, column=2)
buttonA=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick("+"),text="+",bd=10).grid(row=1, column=3)
button4=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(4),text="4",bd=10).grid(row=2, column=0)
button5=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(5),text="5",bd=10).grid(row=2, column=1)
button6=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(6),text="6",bd=10).grid(row=2, column=2)
buttonS=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick("-"),text="-",bd=10).grid(row=2, column=3)
button1=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(1),text="1",bd=10).grid(row=3, column=0)
button2=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(2),text="2",bd=10).grid(row=3, column=1)
button3=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(3),text="3",bd=10).grid(row=3, column=2)
buttonM=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick("*"),text="*",bd=10).grid(row=3, column=3)
buttonC=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=caseClearTextDisplay,text="C",bd=10).grid(row=4, column=0)
button0=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick(0),text="0",bd=10).grid(row=4, column=1)
buttonD=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=lambda:caseClick("/"),text="/",bd=10).grid(row=4, column=2)
buttonE=Button(root,padx=8,pady=8,fg="white",bg="black",font=('arial',15,'bold'),command=caseEqualsInput,text="=",bd=10).grid(row=4, column=3)
root.mainloop()