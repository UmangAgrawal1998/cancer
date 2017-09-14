from tkinter import *
root=Tk()
root.geometry("400x170+100+100")
label_1=Label(wraplength=400,text='The T category describes how far the main tumor has grown into the wall of the bladder (or beyond).'
                                ' Illustration showing the location of the bladder in relation to the kidneys, uterus (in women),'
                                ' prostate (in men), ureter and urethra. There is also a close up showing the layers of the bladder'
                                ' wall with papillary and flat tumors. The wall of the bladder has 4 main layers.,'
                                'The innermost lining is called the urothelium or transitional epithelium.'
                                'Beneath the urothelium is a thin layer of connective tissue, blood vessels, and nerves.'
                                'Next is a thick layer of muscle.'
                                'Outside of this muscle, a layer of fatty connective tissue separates the bladder from other nearby organs.'
                                'Nearly all bladder cancers start in the urothelium. As the cancer grows into or through the other layers'
                                ' in the bladder, it becomes more advanced',background='bisque',foreground='red')
label_1.pack()
root.mainloop()
