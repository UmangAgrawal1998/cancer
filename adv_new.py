from tkinter import *
root=Tk()
root.title("CANCURE: A SOLEMN EFFORT TO CURE CANCER")
root.geometry("700x500+350+200")
bg_col='seashell2'
bg_col1='lavender blush'

def calculation():
    T=str(input('Enter the value of tumor spread: '))
    N=str(input('Enter the value of node: '))
    M=str(input('Enter the value of MetaStasis: '))

    if(M=='M0' and T=='T0' and N=='N0'):
        result='No Primary Tumor Detected'
    elif( T=='Ta' and N=='N0' and M=='M0'):
        result='Development of small transparent layer of tumor on the gland. STAGE 1'
    elif((T=='T2a' or T=='T2b') and M=='M0' and N=='N0'):
        result='Developemnt of thick muscle layer of tumor but not passing through the fatty tissue of the gland, STAGE 2'
    elif((T=='T3a' or T=='T3b') and M=='M0' and N=='N0'):
        result='The tumor has grown into the layer of fatyy tissue that surrounds the gland and might have spread into the gland. STAGE 3'
    elif(T=='T4b' and N=='N0' and M=='M0'):
         result='The Tumor has grown through the organ and into the pelvic wall and no observation for spreading of tumor. STAGE 4'
    elif(T=='T4b' and N=='N1' and M=='M1'):
        result='The Tumor has grown through the organ and into the pelvic wall and spreading of tumor to other organs is observed. STAGE 4'
    print(result)    

        
calculation()

text1=Text(root2,width=20,height=1,background='floral white',foreground='red',font='TimesNewRoman 10')
text1.place(x=800,y=220)
text1.tag_configure("center", justify='center')
text1.tag_add("left", 1.0, "end")
