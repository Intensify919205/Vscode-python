"""import tkinter as t

def on_select(event):
    option.set(event)


#window
w=t.Tk()
w.title("Slam book")
w.geometry("500x500")
w.configure(bg="yellow")
#Label and entry
t.Label(w,text="Fill your details",bg="yellow",fg="green",font=("Aerial",15,"bold")).pack()
t.Label(w,text="Name",bg="yellow",fg="green",font=("Aerial",15,"bold")).place(x=20 ,y=45)
t.Entry(w,width=30,font=("aerial",10,"bold")).place(x=100 ,y=50)
t.Label(w,text="How can I contact you?",bg="yellow",fg="green",font=("Aerial",15,"bold")).place(x=10 ,y=80)
t.Entry(w,width=30,font=("aerial",10,"bold")).place(x=250 ,y=85)
t.Label(w,text="Choose your hobby",bg="yellow",fg="green",font=("Aerial",15,"bold")).place(x=10 ,y=150)
#Checkbutton
t.Checkbutton(w,text="sports",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=10 ,y=180)
t.Checkbutton(w,text="coding",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=120 ,y=180)
t.Checkbutton(w,text="dancing",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=230 ,y=180)
t.Checkbutton(w,text="painting",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=10 ,y=230)
t.Checkbutton(w,text="travelling",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=120 ,y=230)
t.Checkbutton(w,text="skydiving",onvalue=1,offvalue=0,font=("Aerial",15,"bold")).place(x=250 ,y=230)
#RadioButton
t.Label(w,text="What is your gender??",bg="yellow",fg="green",font=("Aerial",15,"bold")).place(x=10 ,y=290)
t.Radiobutton(w,text="Male",value=1,font=("Aerial",15,"bold")).place(x=10 ,y=340)
t.Radiobutton(w,text="female",value=2,font=("Aerial",15,"bold")).place(x=120 ,y=340)
t.Radiobutton(w,text="others",value=3,font=("Aerial",15,"bold")).place(x=250 ,y=340)
#Dropdown
option=t.StringVar()
month=["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
t.OptionMenu(w,option,*month,command= on_select).place(x=120 ,y=390)
option.set("Month")

w.mainloop()
"""

