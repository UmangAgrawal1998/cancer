#PATIENT REGISTRATION FORM

from tkinter import *
from tkinter import ttk

#Default
bg_col='snow'
large_font = ('Cambria',13)


class Feedback:

    def __init__(self,master):


        self.frame_header = ttk.Frame(master)
        self.frame_header.place(x=100,y=100)
        self.style = ttk.Style()
        self.style.configure('TButton', foreground='old lace')
        self.style.configure('TFrame',background=bg_col)
        self.style.configure('TButton', background=bg_col)
        self.style.configure('TLabel', background=bg_col)
        self.style.configure('TLogo', background=bg_col)



        self.logo=PhotoImage(file='freepik.png').subsample(5,5)
        ttk.Label(self.frame_header,image=self.logo).place(x=400,y=650)
        ttk.Label(self.frame_header,text="PATIENT REGISTRATION FORM", background=bg_col,foreground='blue',font="TimesNewRoman 20 underline bold").place(x=50,y=50)
        ttk.Label(self.frame_header, text="Give a detailed information about yourself for our record. Thank You", background=bg_col, foreground='blue',
                  font="TimesNewRoman 15 ").place(x=50,y=50)

        self.frame_content = ttk.Frame(master)
        ttk.Label(self.frame_content, text='Honorific*', background=bg_col, font="Cambria 13").place(x=30,y=30)
        ttk.Entry(self.frame_content, text='Honorific*', background=bg_col, font="Cambria 13").place(x=70,y=70)

        self.frame_content.grid(row=1,column=3,sticky=W)


        #ttk.Label(self.frame_header,text ='Name:').grid(row=1,column=0,padx=5,sticky='sw')
        #ttk.entry_name = ttk.Entry(self.frame_content,width=24).grid(row=1,column=0,padx=5,sticky='sw')
        #self.text_comments = Text(self.frame_content,width=50,height=10).grid(row=3,column=0,padx=5,sticky='w')

        ttk.Button(self.frame_content,text='Submit')


def main():

    root=Tk()
    feedback = Feedback(root)
    root.title("PATIENT FORM")
    root.geometry("700x1000")
    root.configure(background=bg_col)
    root.resizable(False, True)
    root.mainloop()

if __name__=="__main__": main()
