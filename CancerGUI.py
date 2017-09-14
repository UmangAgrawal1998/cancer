from tkinter import *
import webbrowser
root=Tk()
root.title("CANCURE: A SOLEMN EFFORT TO CURE CANCER")
root.geometry("700x500+350+200")
bg_col='seashell2'
bg_col1='lavender blush'

def page1():
    root.destroy()
    import UserLogin

def openpage2():
    root.destroy()
    import CancerGUI2

def page2():
    webbrowser.open("page2.htm");

#Label1
label_1=Label(root,text='CanCure : A Solemn Effort To Cure Cancer',background=bg_col,foreground='coral',font='Cambria 20 bold').place(x=100,y=20)

#BUTTON 1
button_1=Button(root,text='SEARCH FOR CANCER',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=page2)
button_1.place(x=250,y=270)
logo=PhotoImage(file='freepik.png')
small_logo=logo.subsample(5,5)
button_1.config(image=small_logo,compound=LEFT)

button_x=Button(root,text='USER LOGIN',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=page1)
button_x.place(x=0,y=470)
button_1.config(compound=LEFT)

#BUTTON 2
button_2=Button(root,text='CUSTOM SEARCH FOR CANCER',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=openpage2)
button_2.place(x=220,y=150)
logo2=PhotoImage(file='freepik.png')
small_logo2=logo2.subsample(5,5)
button_2.config(image=small_logo2,compound=LEFT)



root.configure(background=bg_col)
root.mainloop()
