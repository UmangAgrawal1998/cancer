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

def printnode():
    root2.destroy()
    import tumor
def printtumor():
    root2.destroy()
    import Definition_File
def printmeta():
    root2.destroy()
    import meta
#BUTTON 1
button_1=Button(root2,text='NODE',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=printnode)
button_1.place(x=200,y=200)
logo=PhotoImage(file='freepik.png')
small_logo=logo.subsample(5,5)
button_1.config(image=small_logo,compound=LEFT,width=300,height=60)

#BUTTON 2
button_2=Button(root2,text='TUMOR',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=printtumor)
button_2.place(x=200,y=350)
logo2=PhotoImage(file='freepik.png')
small_logo2=logo2.subsample(5,5)
button_2.config(image=small_logo2,compound=LEFT,width=300,height=60)

#BUTTON 3
button_3=Button(root2,text='META STAGES',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=printmeta)
button_3.place(x=200,y=500)
logo3=PhotoImage(file='freepik.png')
small_logo3=logo3.subsample(5,5)
button_3.config(image=small_logo3,compound=LEFT,width=300,height=60)

text1=Text(root2,width=20,height=1,background='floral white',foreground='red',font='TimesNewRoman 10')
text1.place(x=800,y=220)
text1.tag_configure("center", justify='center')
text1.tag_add("left", 1.0, "end")


text2=Text(root2,width=20,height=1,background='floral white',foreground='red',font='TimesNewRoman 10')
text2.place(x=800,y=370)


text3=Text(root2,width=20,height=1,background='floral white',foreground='red',font='TimesNewRoman 10')
text3.place(x=800,y=520)

M_num=0
def save_val():
    M_num=0
    val1 = text1.get('1.0', END)
    val2 = text2.get('1.0', END)
    val3 = text3.get('1.0', END)
    T = str(val2)
    N = str(val1)
    M = val3

    tbox = Text(root2, width=50, height=3, background='floral white', foreground='red', font='TimesNewRoman 13')
    result=''
    if ("M0" in M and "T0" in T and "N0" in N):
        result += 'No Primary Tumor Detected'
    elif ("Ta" in T and "N0" in N and "M0" in M):
        result += 'Development of small transparent layer of tumor on the gland. STAGE 1'
    elif (("T2a" in T or "T2b" in T) and "M0" in M and "N0" in N):
        result += 'Developemnt of thick muscle layer of tumor but not passing through the fatty tissue of the gland, STAGE 2'
    elif (("T3a" in T or "T3b" in T) and "M0" in M and "N0" in N):
        result += 'The tumor has grown into the layer of fatyy tissue that surrounds the gland and might have spread into the gland. STAGE 3'
    elif ("T4b" in T and "N0" in N and "M0" in M):
        result = 'The Tumor has grown through the organ and into the pelvic wall and no observation for spreading of tumor. STAGE 4'
    elif ("T4b" in T and "N1" in N and "M1" in M):
        result += 'The Tumor has grown through the organ and into the pelvic wall and spreading of tumor to other organs is observed. STAGE 4'

    tbox.insert('1.0', result)
    tbox.place(x=500, y=700)

button_4=Button(root2,text='SUBMIT',background=bg_col1,foreground='coral1',font="TimesNewRoman 10 underline bold",command=save_val)
button_4.place(x=600,y=630)
button_4.config(compound=LEFT,width=20,height=2)




root2.configure(background=bg_col)
root2.mainloop()
