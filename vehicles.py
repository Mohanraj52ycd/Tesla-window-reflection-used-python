from tkinter import *
import tkinter as tk
from tkvideo import tkvideo
import webbrowser
from PIL import Image, ImageTk




w1 = tk.Tk()
def New1():
    print("Button clicked")
def open_line1():
    webbrowser.open('https://www.tesla.com///models//design#overview')

def open_line2():
    webbrowser.open('https://www.tesla.com//model3')


def open_line3():
    webbrowser.open('https://www.tesla.com//modelx')
def open_line4():
    webbrowser.open('https://www.tesla.com//modely')
def open_line5():
    webbrowser.open('https://www.tesla.com//cybertruck')
def open_line6():
    webbrowser.open('https://www.tesla.com/choose')

def open_line7():
    webbrowser.open("https://www.tesla.com//inventory//new//my?arrangeby=relevance&range=0")


def open_line8():
    webbrowser.open("https://www.tesla.com//inventory//used//my?arrangeby=plh")


def open_line9():
    webbrowser.open("https://www.tesla.com//drive")


def open_line10():
    webbrowser.open("https://www.tesla.com//tradein")



def open_line11():
    webbrowser.open("https://www.tesla.com//compare")



def open_line12():
    webbrowser.open("https://www.tesla.com//charge")

def open_line13():
    webbrowser.open("https://www.tesla.com//fleet")

def open_line14():
    webbrowser.open("https://www.tesla.com//semi")

def open_line15():
    webbrowser.open("https://www.tesla.com//roadster")

w1.wm_state("zoomed")
w1.title("ＴΞＳＬΛ")
iconimg1 = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon1 = ImageTk.PhotoImage(iconimg1)
w1.iconphoto(False, tkicon1)


w1.configure(bg="black")
video_labell = Label(w1)
video_labell.pack()
video_labell.place(x=810,y=150)
player = tkvideo("C:\\mohan\\tesla\\image and videos\\w2video1.webm"
                 , video_labell, loop=1, size=(550, 550))
player.play()

l=Label(w1,text='ＴΞＳＬΛ',bg='black',fg='white',font=('Helvetica',20))
l.place(x=0,y=25)
l=Label(w1,text='Tesla Car Models',bg='black',fg='white',font=('Helvetica',20))
l.place(x=5,y=180)

Dimensions ='C:\\mohan\\tesla\\image and videos\\w2tesla blue print.jpg'
Dimensionss = Image.open(Dimensions)
Dimensionss= Dimensionss.resize((550, 550))
Dimensionsss=ImageTk.PhotoImage(Dimensionss)


model_s_label = Label(w1, image=Dimensionsss, bg="black")
model_s_label.place(x=260, y=150)




model_s ='C:\\mohan\\tesla\\image and videos\\w2tesla s.jfif'
model_ss = Image.open(model_s)
model_ss= model_ss.resize((95, 90))
model_sss=ImageTk.PhotoImage(model_ss)

model_s_label = Label(w1, image=model_sss, bg="black")
model_s_label.place(x=5, y=250)


model_y= "C:\\mohan\\tesla\\image and videos\\w2tesla y.jfif"
model_yy = Image.open(model_y)
model_yy= model_yy.resize((90, 85))
model_yyy= ImageTk.PhotoImage(model_yy)

model_y_label = Label(w1, image=model_yyy, bg="black")
model_y_label.place(x=135, y=250)




model_3= "C:\\mohan\\tesla\\image and videos\\w2tesla 3.jpg"
model_33 = Image.open(model_3)
model_33= model_33.resize((95, 90))
model_333= ImageTk.PhotoImage(model_33)

model_s_label = Label(w1, image=model_333, bg="black")
model_s_label.place(x=5, y=400)

cybertruck= "C:\\mohan\\tesla\\image and videos\\w2cybertruk.jfif"
cybertruckk= Image.open(cybertruck)
cybertruckk= cybertruckk.resize((90, 85))
cybertruckkk= ImageTk.PhotoImage(cybertruckk)

cybertruckkk_label= Label(w1, image=cybertruckkk, bg="black")
cybertruckkk_label.place(x=135, y=400)


model_x= "C:\\mohan\\tesla\\image and videos\\w2tesla x.jfif"
model_xx = Image.open(model_x)
model_xx= model_xx.resize((95, 90))
model_xxx= ImageTk.PhotoImage(model_xx)

model_x_label = Label(w1, image=model_xxx, bg="black")
model_x_label.place(x=5, y=550)


help= "C:\\mohan\\tesla\\image and videos\\w2he.jfif"
helpp= Image.open(help)
helpp= helpp.resize((90, 85))
helppp= ImageTk.PhotoImage(helpp)

help_label = Label(w1, image=helppp, bg="black")
help_label.place(x=135, y=550)


button_font = ('Helvetica', 13)
button_width = 10
button_height = 0

b1 = Button(w1, text="Model S", command=open_line1, font=button_font, bg="black", fg="white", width=button_width, height=button_height)
b1.place(x=5, y=350)

b2 = Button(w1, text="Model 3", command=open_line2, font=button_font, bg="black", fg="white", width=button_width, height=button_height)
b2.place(x=5, y=500)

b3 = Button(w1, text="Model X", command=open_line3, font=button_font, bg="black", fg="white", width=button_width, height=button_height)
b3.place(x=5, y=650)

b4 = Button(w1, text="Model Y", command=open_line4, font=button_font, bg="black", fg="white", width=button_width, height=button_height)
b4.place(x=135, y=350)

b5 = Button(w1, text="Cybertruck", command=open_line5,
            font=button_font, bg="black", fg="white", width=button_width, height=button_height)
b5.place(x=135, y=500)

b6 = Button(w1, text="Help Me Choose", command=open_line6, font=button_font, bg="black", fg="white",
            width=button_width+3, height=button_height-1)
b6.place(x=120, y=650)


b7 = Button(w1, text="Inventory", command=open_line7,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b7.place(x=50, y=100)


b8 = Button(w1, text="Used Cars", command=open_line8,
            font=button_font, bg="black",fg="white", width=button_width, height=button_height)
b8.place(x=200, y=100)


b9 = Button(w1, text="Demo Drive", command=open_line9,
            font=button_font, bg="black",fg="white", width=button_width, height=button_height)
b9.place(x=350, y=100)

b10 = Button(w1, text="Trade-in", command=open_line10,
            font=button_font, bg="black",fg="white", width=button_width, height=button_height)
b10.place(x=500, y=100)

b11 = Button(w1, text="Compare", command=open_line11,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b11.place(x=650, y=100)

def back():
    w1.destroy()
    import testla
def next():
    w1.destroy()
    import Energy

b13=Button(w1,text="Back",command=back,bg="black",fg="red")
b13.place(x=1280,y=0)

b14 = Button(w1, text="next", command=next, bg="black", fg="red")
b14.place(x=1323, y=0)

b12 = Button(w1, text="Help Me Charge", command=open_line12,
            font=button_font,bg="black",fg="white", width=button_width+4, height=button_height)
b12.place(x=800, y=100)



b13 = Button(w1, text="Fleet", command=open_line13,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b13.place(x=980, y=100)


b14 = Button(w1, text="Semi", command=open_line14,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b14.place(x=1120, y=100)

b15= Button(w1, text="Roadster", command=open_line15,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b15.place(x=1250, y=100)

w1.mainloop()
