from tkinter import *
root=Tk()
root.geometry("700x500+350+0")

import mysql.connector
con = mysql.connector.connect(user='root',
                              password ='root',
                              host='localhost',
                              database='hackathon')

cur = con.cursor()

query = ("SELECT hosname,city from hosbreast")
   

cur.execute(query)
l=[]
k=[]
for (hosname, city) in cur:
  l.append(hosname)
  k.append(city)
  #script=print("{} in {} \n".format(hosname,city))
t = Text(root)
p=Text(root)
for x in l:
    t.insert(END, x + '\n')
t.place(x=70,y=10)
t.configure(background='pink',font=('TimesNewRoman',(10)))


for i in k:
    p.insert(END,i+'\n')
p.place(x=350,y=10) 
p.configure(background='snow')

root.mainloop()
cur.close()
con.close()
