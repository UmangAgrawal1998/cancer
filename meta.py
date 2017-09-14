from tkinter import *
root=Tk()
root.geometry("380x50+100+100")
label_1=Label(wraplength=400,text='M0: There are no signs of distant spread.'
                                  'M1: The cancer has spread to distant parts of the body. (The most common sites are distant lymph nodes,'
                                  ' the bones, the lungs, and the liver.)',background='bisque',foreground='red')
label_1.pack()
root.mainloop()
