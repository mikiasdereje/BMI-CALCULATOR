from tkinter import*

#------------------------------------------------------
def calculate ():# DEFINING THE FORMULA
    height=float(e1.get())
    weidth=float(e2.get())
    bmi = weidth/height**2 # <==THE BMI FORMULA

    if bmi<=18.5:
         e3.configure(text="you'r under weight,bmi= {:.1f}".format(bmi))
    elif bmi <=24.99:
         e3.configure(text="you'r healthy,bmi= {:.1f}".format(bmi))
    elif bmi<=29.99:
        e3.configure(text="you'r over weight,bmi= {:.1f}".format(bmi))
    elif bmi>=30:
        e3.configure(text="you'r obses because you'r bmi is {:.1f}".format(bmi))
#-------------------------------------------------------
def delete ():
    e3.config(text="")# <== to delet text in the label
miko=Tk()

#-------------------------------------------------------
miko.maxsize(height=440,width=470)#CHANGING THE SIZE
miko.minsize(height=440,width=470)
#--------------------------------------------------------
miko.title('BMI CALCULATOR')#CHANGING THE TITLE
#--------------------------------------------------------
miko.config(bg="#13124a")#CHANGING THE COLOR
#--------------------------------------------------------
miko.wm_attributes('-toolwindow',True)#iliminating the icon
#---------------------------------------------------------
e1=Entry(miko,font=('bold',19),width=12,bg="#878b91",bd=5)#FIRST ENTERY BOX
e1.place(x=10,y=60)
#---------------------------------------------------------
e2=Entry(miko,font=('bold',19),width=12,bg="#878b91",bd=5)#second ENTERY BOX
e2.place(x=280,y=60)
#---------------------------------------------------------
l1=Label(miko,font=('bold',20),text="height(m):",bg="#13124a",fg="#f0f2f5")#TEXT HEIGHT
l1.place(x=10,y=20)
#---------------------------------------------------------
l2=Label(miko,font=('bold',20),text="weight(kg):",bg="#13124a",fg="#f0f2f5")#TEXT WEIDTH
l2.place(x=280,y=20)
#----------------------------------------------------------
b1=Button(miko,text="enter",font=("bold",10),width=25,height=2,bg="#01031a",fg="#ffffff",
                        activebackground="#4e5487",bd=1,command=calculate)#ENTER BUTTON
b1.place(x=140,y=140)
#-----------------------------------------------------------
l3=Label(miko,font=('bold',20),text="BMI:",bg="#13124a",fg="#f0f2f5")#TEXT BMI
l3.place(x=10,y=200)
#-----------------------------------------------------------
e3=Label(miko,font=('bold',20),text="---",bg="#878b91",width=28)#OUTPUT
e3.place(x=10,y=240)
#-----------------------------------------------------------
b2=Button(miko,text="delete",font=("bold",10),width=25,height=2,bg="#192f8a",fg="#ffffff",
                        activebackground="#4e5487",bd=1,command=delete)
b2.place(x=260,y=290)
#-----------------------------------------------------------

miko.mainloop()
