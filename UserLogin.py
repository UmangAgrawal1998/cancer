from tkinter import *
root=Tk()
import mysql.connector
def inser(n,d,a,g,o,m,ad):
    con = mysql.connector.connect(user='root',
                              password ='root',
                              host='localhost',
                              database='hackathon')

    cur = con.cursor()
    #insert new student details
    cur.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s)",(n,d,a,g,o,m,ad) )
    con.commit()
    cur.close()
    con.close()

#Default
bg_col='bisque'
bg_col1='antique white'
fg_col1='blue'
large_font = ('Cambria',13)

#Main Window
root.title("PATIENT FORM")
root.geometry("700x1300+400+0")
root.configure(background=bg_col)
root.resizable(True, True)

#Widgets

#logo=PhotoImage(file='images.png').subsample(3,3)
#Label(image=logo).place(x=30,y=10)
#logo.config(bg=bg_col)
mainlabel=Label(text='Patient Registration Form ',background=bg_col,foreground='blue',font='TimesNewRoman 30 underline bold ').place(x=130,y=13)
label_1=Label(text='Honorific*', background=bg_col, font="Cambria 13").place(x=20,y=110)

def new_window():

    root.destroy()
    root2 = Tk()
    root2.title("PATIENT FORM")
    root2.geometry("700x1300+400+0")
    root2.configure(background=bg_col)
    root2.resizable(False, True)

    def submit():
        global address
        global mobile
        global email
        global to_which
        global refer
        global sign
        global date

        address=text.get('1.0',END)
        mobile=entry_1.get()
        email=entry_3.get()
        to_which=entry_4.get()
        refer=entry_5.get()
        sign=entry_6.get()
        date=entry_7.get()

                
        
        root2.destroy()



    mainlabel = Label(text='Patient Registration Form ', background=bg_col, foreground='blue',
                      font='TimesNewRoman 30 underline bold ').place(x=130, y=13)

    label_4 = Label(text='Permanent Addresss & Pincode*', background=bg_col, font="Cambria 13").place(x=20, y=550)
    text=Text(root2,width=60,height=5,background='floral white',foreground='red')
    text.place(x=50,y=610)
    address=text.get('1.0',END)


    label_11 = Label(text='Mobile', background=bg_col, font="Cambria 13").place(x=20, y=130)
    entry_1=Entry(root2,width=30)
    entry_1.configure(background=bg_col1,foreground=fg_col1)


    label_13 = Label(text='E-Mail', background=bg_col, font="Cambria 13").place(x=20, y=200)
    entry_3=Entry(root2,width=50)
    entry_3.configure(background=bg_col1, foreground=fg_col1)


    label_14 = Label(text='To Visit Which (Doctor/Hospital)', background=bg_col, font="Cambria 13").place(x=20, y=270)
    entry_4 = Entry(root2, width=50)
    entry_4.configure(background=bg_col1, foreground=fg_col1)


    label_15 = Label(text='Referred by Doctor', background=bg_col, font="Cambria 13").place(x=20, y=340)
    entry_5 = Entry(root2, width=50)
    entry_5.configure(background=bg_col1, foreground=fg_col1)


    label_16 = Label(text='Signature of:   1.Patient     2.Doctor', background=bg_col, font="Cambria 13").place(x=20, y=410)
    entry_6 = Entry(root2, width=50)
    entry_6.configure(background=bg_col1, foreground=fg_col1)


    label_17 = Label(text='Date Of Registration', background=bg_col, font="Cambria 13").place(x=20, y=480)
    entry_7 = Entry(root2, width=30)
    entry_7.configure(background=bg_col1, foreground=fg_col1)

    def cleartext():

        entry_1.delete(0,END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_7.delete(0, END)
        text.delete('1.0',END)

    button_2 = Button(text='Submit', background=bg_col, font='TimesNewRoman 15',command=submit).place(x=100, y=750)
    button_3 = Button(text='Clear', background=bg_col, font='TimesNewRoman 15', command=cleartext).place(x=400, y=750)

    entry_1.place(x=300, y=135)
    entry_3.place(x=300, y=205)
    entry_4.place(x=300, y=275)
    entry_5.place(x=300, y=345)
    entry_6.place(x=300, y=415)
    entry_7.place(x=300, y=485)

    root2.mainloop()

var = StringVar(root)
var.set('Select')
choices = {'Select':0, 'Mr.':1, 'Mrs.':2, 'Dr.':3,'Master':4, 'Miss.':5}
option = OptionMenu(root,var, *choices)
option.config(font=('Cambria',(13)),bg='lemon chiffon')
option['menu'].config(font=('Calibri',(13)),bg='lemon chiffon')
age = StringVar()
def change_age(*args):
    age_ = choices[var.get()]
    age.set(age_)
# trace the change of var
var.trace('w', change_age)

label_2=Label(text='Patient Name*', background=bg_col, font="Cambria 13").place(x=20,y=180)
entry_1=Entry(root,width=50)
entry_1.place(x=300,y=185)
entry_1.configure(background=bg_col1, foreground=fg_col1)

value='No'
#r1_1=RADIOBUTTON(text='Yes',value='Yes')
#r1_2=RADIOBUTTON(text='No',value='No')

label_3=Label(text='Are you medically insured?*', background=bg_col, font="Cambria 13").place(x=20,y=250)

label_4=Label(text='Gender*', background=bg_col, font="Cambria 13").place(x=20,y=320)

label_5=Label(text='Marital Status*', background=bg_col, font="Cambria 13").place(x=20,y=390)

label_6=Label(text='Date of Birth*', background=bg_col, font="Cambria 13").place(x=20,y=460)

label_7=Label(text='Age', background=bg_col, font="Cambria 13").place(x=20,y=530)

label_8=Label(text='Occupation*', background=bg_col, font="Cambria 13").place(x=20,y=600)

label_9=Label(text='Language*', background=bg_col, font="Cambria 13").place(x=20,y=670)

entry_2=Entry(root,width=50)
entry_2.place(x=300,y=325)
entry_2.configure(background=bg_col1, foreground=fg_col1)
entry_3=Entry(root,width=50)
entry_3.place(x=300,y=395)
entry_3.configure(background=bg_col1, foreground=fg_col1)
entry_4=Entry(root,width=50)
entry_4.place(x=300,y=465)
entry_4.configure(background=bg_col1, foreground=fg_col1)
entry_5=Entry(root,width=50)
entry_5.place(x=300,y=535)
entry_5.configure(background=bg_col1, foreground=fg_col1)
entry_6=Entry(root,width=50)
entry_6.place(x=300,y=605)
entry_6.configure(background=bg_col1, foreground=fg_col1)
entry_9=Entry(root,width=50)
entry_9.place(x=300,y=675)
entry_9.configure(background=bg_col1, foreground=fg_col1)
entry_7=Entry(root,width=50)
entry_8=Entry(root,width=50)
entry_8.configure(background=bg_col1, foreground=fg_col1)
entry_8.place(x=300,y=255)
entry_7.configure(background=bg_col1, foreground=fg_col1)
entry_7.place(x=300,y=675)


def submit():
    global Gender
    global name
    global insured
    global honorific
    global marital
    global dob
    global age
    global occupation
    global lang

    name = entry_1.get()
    Gender = entry_2.get()
    insured = entry_8.get()
    #honorific = entry_15.get()
    marital = entry_3.get()
    dob = entry_4.get()
    age = entry_5.get()
    occupation=entry_6.get()
    lang=entry_9.get()
    new_window()
    na=name
    da=dob
    ae=age
    ge=Gender
    oc=occupation
    mo=mobile
    ad=address
    inser(na,da,ae,ge,oc,mo,ad)
    


def cleartext():
    var.set('Select')
    entry_1.delete(0,END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    entry_2.delete(0,END)
    entry_8.delete(0,END)

button_2=Button(text='Clear',background=bg_col,font="Cambria 13",command=cleartext).place(x=400,y=740)
button_1=Button(text='Page 2',background=bg_col,font="Cambria 13",command=submit).place(x=200,y=740)

option.place(x=250,y=110)
root.mainloop()
