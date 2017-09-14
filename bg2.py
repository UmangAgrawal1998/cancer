from tkinter import *
root=Tk()
root.geometry("5000x5000")

import mysql.connector
con = mysql.connector.connect(user='root',
                              password ='root',
                              host='localhost',
                              database='hackathon')

cur = con.cursor()

query = ("SELECT doctorname,speciality,hospital from doctor")
   

cur.execute(query)
l=[]
k=[]
j=[]
for (doctorname, speciality,hospital) in cur:
  l.append(doctorname)
  k.append(speciality)
  j.append(hospital)
  #script=print("{} in {} \n".format(hosname,city))
t = Text(root)
p=Text(root)
q=Text(root)
for x in l:
    t.insert(END, x + '\n')
t.place(x=70,y=10)
t.configure(background='pink',font=('TimesNewRoman',(10)))

for y in j:
  q.insert(END,y+'\n')
q.place(x=700,y=10)
q.configure(background='bisque',font=("TimesNewRoman",(10)))
  
for i in k:
    p.insert(END,i+'\n')
p.place(x=350,y=10) 
p.configure(background='snow')

root.mainloop()
cur.close()
con.close()
