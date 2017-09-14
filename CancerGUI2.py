from tkinter import *
root2=Tk()
root2.title("CANCURE: A SOLEMN EFFORT TO CURE CANCER (CS LINK)")
root2.geometry("5000x5000")
bg_col1='lavender blush'
bg_col='lemon chiffon'


#Label1
label_1=Label(root2,text='CanCure : A Solemn Effort To Cure Cancer',background=bg_col,foreground='coral',font='Cambria 20 bold').place(x=500,y=20)

#Label2
label_2=Label(root2,text='SEARCH RESULTS',background=bg_col,foreground='red3',font='Cambria 20 bold').place(x=650,y=80)

def hospital():
    import bg


def calladv():
    root2.destroy()
    import advanced_search
def doctor():
    import bg2
#BUTTON 1
button_1=Button(root2,text='ADVANCED SEARCH',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=calladv)
button_1.place(x=600,y=200)
logo=PhotoImage(file='freepik.png')
small_logo=logo.subsample(5,5)
button_1.config(image=small_logo,compound=LEFT,width=300,height=60)

#BUTTON 2
button_2=Button(root2,text='HOSPITAL/CENTER FOR TREATMENT RESULTS',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=hospital)
button_2.place(x=560,y=350)
logo2=PhotoImage(file='freepik.png')
small_logo2=logo2.subsample(5,5)
button_2.config(image=small_logo2,compound=LEFT,width=400,height=60)

#BUTTON 2
button_3=Button(root2,text='DOCTOR OR SPECIALIST RESULTS',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=doctor)
button_3.place(x=605,y=500)
logo3=PhotoImage(file='freepik.png')
small_logo3=logo3.subsample(5,5)
button_3.config(image=small_logo3,compound=LEFT,width=300,height=60)


root2.configure(background=bg_col)
root2.mainloop()
