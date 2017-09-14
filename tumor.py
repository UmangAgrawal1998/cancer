from tkinter import *
root=Tk()
root.geometry("400x170+100+100")
label_1=Label(wraplength=400,text='The N category describes spread only to the lymph nodes near the bladder (in the true pelvis) '
                                  'and those along the blood vessel called the common iliac artery. These lymph nodes are called regional'
                                  ' lymph nodes. Any other lymph nodes are considered distant lymph nodes. Spread to distant nodes'
                                  ' is considered metastasis (described in the M category). Surgery is usually needed to find cancer '
                                  'spread to lymph nodes, since it is not often seen on imaging tests.'
                                  'NX: Regional lymph nodes cannot be assessed due to lack of information.'
                                  'N0: There is no regional lymph node spread.'
                                  'N1: The cancer has spread to a single lymph node in the true pelvis.'
                                  'N2: The cancer has spread to 2 or more lymph nodes in the true pelvis.'
                                  'N3: The cancer has spread to lymph nodes along the common iliac artery.',background='bisque',foreground='red')
label_1.pack()
root.mainloop()
