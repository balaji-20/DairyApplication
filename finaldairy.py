from tkinter import *
from tkcalendar import *
from tkinter import messagebox
def mainscreen():
    def button():
        if(b1['text']=='Create'):
            b1['text']='Check'
            c1.configure(state=DISABLED)
            c2.configure(state=NORMAL)
            msg.delete("1.0","end")
    
        else:
            b1['text']='Create'
            c2.configure(state=DISABLED)
            c1.configure(state=NORMAL)
            msg.delete("1.0","end")
    def save():
        d=entry.get()
        t=msg.get(1.0,"end")
        try:
            f=open("dairy.txt",'r')
            lines=f.readlines()
            e=d+"\n"
            if e not in lines:
                x="\n"+d+"\n"+t+"$\n"
                f=open("dairy.txt",'a')
                for a in x:
                    f.write(a)
                f.close()
                entry.delete(0,END)
                msg.delete("1.0","end")

            else:
                messagebox.showerror("Error", "Date already exists")
        except:
            f=open("dairy.txt",'w')

    def display():
        try:
            msg.delete("1.0","end")
            e=entry.get()
            x=e+"\n"
            f=open("dairy.txt",'r')
            lines=f.readlines()
            t=lines.index(x)
            for i in range(t+1,100):
                if(lines[i]=="$\n"):
                    break
                msg.insert(INSERT,lines[i])
        except:
            messagebox.showinfo("", "No Data Found")    
    MW.geometry("700x600")
    s2=Frame(MW,height=600, width=700)
    s2.pack()
    
    background_image = PhotoImage(file='background.png')
    background_label = Label(s2, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    bframe = Frame(s2, bg='black', bd=3)
    bframe.place(relx=0,rely=0.04,relheight=0.08,relwidth=0.2,anchor='w')
    b1=Button(bframe,text="Check",command=lambda: button(),font=40)
    b1.place(relheight=1,relwidth=1)
  
    frame = Frame(s2, bg='black', bd=3)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    Label(frame,text="Enter Date",font=40).place(relheight=1, relwidth=0.3)

    entry=DateEntry(frame,font=40)
    entry.place(relx=0.35, relheight=1, relwidth=0.65)

    cframe = Frame(s2, bg='black', bd=3)
    cframe.place(relx=0.5,rely=0.22,relheight=0.1,relwidth=0.3,anchor='n')

    c1=Button(cframe,text="View Notes",command=lambda: display(),font=40,state=DISABLED)
    c1.place(relheight=1,relwidth=1)

    lframe=Frame(s2,bg='black', bd=3)
    lframe.place(relx=0.5, rely=0.34, relwidth=0.75, relheight=0.5, anchor='n')

    msg=Text(lframe,font=35)
    msg.place(relwidth=1, relheight=1)

    dframe = Frame(s2, bg='black', bd=3)
    dframe.place(relx=0.5,rely=0.86,relheight=0.1,relwidth=0.3,anchor='n')

    c2=Button(dframe,text="Save Notes",command=lambda:save(),font=40)
    c2.place(relheight=1,relwidth=1)
    MW.mainloop()
    
    
def bro():
    if txt.get()=="delhi":
        root.destroy()
        mainscreen()
    else:
        messagebox.showerror("", "Incorrect Password")
MW=Tk()
MW.geometry("300x100")
root=Frame(MW,height=100,width=302)
root.pack()
Label(root,text="Enter Password").grid(row=0,column=0,padx=5,pady=20)
txt=Entry(root,show="*",width=30)
txt.grid(row=0,column=1,pady=20)
Label(root,text="Hint: India Capital",fg='red').grid(row=3,column=0)
b=Button(root,text="ok",width=10,command=bro)
b.grid(row=3,column=1)

