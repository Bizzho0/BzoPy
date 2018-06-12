#vp_BZOm1.py

from tkinter import *
#import BZOm1
#print(dir(BZOm1))
#bzo_resul= BZOm1.f3_dir()
vp=Tk()
vp.title(" °|BZOm1|° ")
#vp.iconbitmap("imagen.ico")
vp.config(bg="dark grey")
#vp.geometry("650x350")
#**********************************************************************
#**********************************************************************
#-----------------------------------------------------
frame0 = Frame(vp, relief=RIDGE, borderwidth=2)
frame0.pack(fill=BOTH,expand=1)
#-----------------------------------------------------
label0 = Label(frame0, text="Hello, _F3NiX_")
label0.pack(fill=X, expand=1)
#**********************************************************************
#**********************************************************************
#-----------------------------------------------------
l_Relieves=['flat', 'groove', 'raised', 'ridge', 'solid','sunken']
frame1=Frame()
frame1.pack(fill="y", expand="True")
frame1.config(bg="purple")
frame1.config(width="400", height="600")
frame1.config(bd=15)
frame1.config(relief=l_Relieves[5])
frame1.config(cursor="pirate") #"hand2"
#-----------------------------------------------------
#label1 = Label(frame1, text=bzo_resul)
#label1.pack(fill="y", expand="True")
#**********************************************************************
#**********************************************************************
#-----------------------------------------------------
frame2 = Frame(vp, relief=RIDGE, borderwidth=2)
frame2.pack(fill=BOTH,expand=1)
#-----------------------------------------------------
label = Label(frame2, text="Bye, _F3NiX_")
label.pack(fill=X, expand=1)
#-----------------------------------------------------
button = Button(frame2,text="SALIR",command=vp.destroy)
button.pack(side=BOTTOM)





vp.mainloop()
