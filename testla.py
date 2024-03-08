import webbrowser
import tkinter as tk
from tkinter import ttk, Label, Button
from PIL import Image, ImageTk
from tkvideo import tkvideo


r=tk.Tk()
button_font1 = ('Helvetica', 13)
button_width = 10
button_height = 0

def add_lin1(tex_one):
   tex_one.insert(tk.END)

tex1=tk.Text
def open_line1():
    webbrowser.open('https://www.tesla.com//cybertruck//design#payment')


def open_line2():
    webbrowser.open("https://www.tesla.com//cybertruck")


def open_line3():
    webbrowser.open('https://www.tesla.com//support')




def open_line6():
    webbrowser.open('https://www.tesla.com//inventory//new//my?arrangeby=relevance&range=0')



r.title("ＴΞＳＬΛ")
r.configure(bg="black")

r.wm_state('zoomed')
iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
r.iconphoto(False, tkicon)

video_label1 = Label(r)
video_label1.place(x=0,y=50)
player1 = tkvideo("C:\\mohan\\tesla\\image and videos\\w1video1.mp4"
                  , video_label1, loop=1, size=(700, 350))
player1.play()

video_label2 = Label(r)
video_label2.place(x=0,y=400)
player2 = tkvideo("C:\\mohan\\tesla\\image and videos\\w1video2.mp4"
                  , video_label2, loop=1, size=(701, 350))
player2.play()

video_label3 = Label(r)
video_label3.place(x=704,y=50)
player3 = tkvideo("C:\\mohan\\tesla\\image and videos\\w1video3.webm"
                  , video_label3, loop=1, size=(700, 350))
player3.play()
video_label4 = Label(r)
video_label4.place(x=700,y=400)
player4 = tkvideo("C:\\mohan\\tesla\\image and videos\\w1video4.webm"
                  , video_label4, loop=1, size=(701, 350))
player4.play()


l=Label(r,text='ＴΞＳＬΛ',bg='black',fg='white',font=('Helvetica',20))
l.place(x=30,y=10)



def vehicles():
    r.destroy()
    import vehicles
def energy():
    r.destroy()
    import Energy
def chaging():
    r.destroy()
    import Charging
def discover():
    r.destroy()
    import Discover
def shop():
    r.destroy()
    import shop


b9 = Button(r, text="Shop Available", command=open_line6, font=button_font1,
           bg="black",fg="white",
            width=button_width+3, height=button_height-1)
b9.place(x=1000, y=680)




q_imag = "C:\\mohan\\tesla\\image and videos\\w1qustion.jpeg"
im_q = Image.open(q_imag)
im_q = im_q.resize((20, 20))
tk_img = ImageTk.PhotoImage(im_q)


img_label = Label(r, image=tk_img, bg="black")
img_label.place(x=1180, y=10)
img_label.bind("<Button-1>", lambda e: open_line3())

w_imag1 = "C:\\mohan\\tesla\\image and videos\\w1world.jpeg"
im_w1 = Image.open(w_imag1)
im_w1= im_w1.resize((20, 20))
tk_img1 = ImageTk.PhotoImage(im_w1)

img_label1 = Label(r, image=tk_img1, bg="black")
img_label1.place(x=1220, y=10)
img_label1.bind("<Button-1>", lambda e: open_line4())


h_imag2 = "C:\\mohan\\tesla\\image and videos\\w1human.jpeg"
im_h2 = Image.open(h_imag2)
im_h2= im_h2.resize((20, 20))
tk_img2 = ImageTk.PhotoImage(im_h2)

img_label2 = Label(r, image=tk_img2, bg="black")
img_label2.place(x=1260, y=10)
img_label2.bind("<Button-1>", lambda e: open_line5())

b1=Button(r,text="vehicles",command=vehicles,bg="black",fg="white",width=0,height=0,font=('Helvetica',13))
b1.place(x=450,y=15)
b2=Button(r,text="Energy",command=energy,bg="black",fg="white",width=0,height=0,font=('Helvetica',13))
b2.place(x=560,y=15)
b3=Button(r,text="Charging",command=chaging,bg="black",fg="white",width=0,height=0,font=('Helvetica',13))
b3.place(x=670,y=15)
b4=Button(r,text="Discover",command=discover,bg="black",fg="white",width=0,height=0,font=('Helvetica',13))
b4.place(x=790,y=15)

b5=Button(r,text="Shop",command=shop,bg="black",fg="white",width=0,height=0,font=('Helvetica',13))
b5.place(x=900,y=15)

l=Label(r,text='ＴΞＳＬΛ',bg='black',fg='white',font=('Helvetica',20))
l.place(x=30,y=10)


do_you=Label(r,text='█▓▒▒░░░Do you Want to Explore these Options? Click on...░░░▒▒▓█',bg='black',fg='white',font=('Helvetica',14))
do_you.place(x=740,y=420)

r.mainloop()
