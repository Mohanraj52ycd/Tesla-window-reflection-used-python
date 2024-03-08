from tkinter import *
import tkinter as tk
from tkvideo import tkvideo
from PIL import Image, ImageTk
import webbrowser

def open_line1():
    webbrowser.open('https://www.tesla.com//solarpanels')

def open_line2():
    webbrowser.open('https://www.tesla.com//solarroof')


def open_line3():
    webbrowser.open('https://www.tesla.com//powerwall')
def open_line4():
    webbrowser.open('https://www.tesla.com//megapack')

def open_line5():
    webbrowser.open("https://www.tesla.com//solar-virtual-consultations")


def open_line6():
    webbrowser.open("https://www.tesla.com//why-solar")


def open_line7():
    webbrowser.open("https://www.tesla.com//support//energy//powerwall//learn/incentives")


def open_line8():
    webbrowser.open("https://www.tesla.com//support//energy/powerwall//installer-resources//partner-with-tesla")



def open_line9():
    webbrowser.open("https://www.tesla.com//commercial")



def open_line10():
    webbrowser.open("https://www.tesla.com//utilities")

def open_line11():
    webbrowser.open("https://www.tesla.com//energy")

w2 = tk.Tk()
w2.title("ＴΞＳＬΛ")
w2.wm_state("zoomed")
w2.configure(bg="black")

video=Label(w2)
video.place(x=0,y=60)
play=tkvideo("C:\\mohan\\tesla\\image and videos\\w2solar-assessment-desktop.mp4"
             ,video,loop=1,size=(550,300))
play.play()


videoo=Label(w2)
videoo.place(x=500,y=362)
playy=tkvideo("C:\\mohan\\tesla\image and videos\w2Tesla Powerwall ｜ Short Video.mp4",videoo,size=(500,340))
playy.play()

solar='C:\\mohan\\tesla\\image and videos\\w2tesla-mobile-app-myhome-powerflow-screen.jpg'
solarr= Image.open(solar)
solarr= solarr.resize((600, 300))
solarrr=ImageTk.PhotoImage(solarr)

solar_label = Label(w2, image=solarrr, bg="black")
solar_label.place(x=500, y=60)
solar_label.bind("<Button-1>",lambda e:open_line11())

l=Label(w2,text='ＴΞＳＬΛ',bg='black',fg='white',font=('Helvetica',25))
l.place(x=2,y=6)

iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
w2.iconphoto(False, tkicon)


solar_panels="C:\\mohan\\tesla\\image and videos\\w22Solar Panels.jfif"
solar_panelss=Image.open(solar_panels)
solar_panelss=solar_panelss.resize((100,100))
solar_solar_panelsss=ImageTk.PhotoImage(solar_panelss)

solar_panelss_label=Label(w2,image=solar_solar_panelsss,bg="black")
solar_panelss_label.place(x=50,y=500)

solarroof="C:\\mohan\\tesla\\image and videos\\w22solarroof.jfif"
solarrooff=Image.open(solarroof)
solarrooff=solarrooff.resize((100,100))
solarroofff=ImageTk.PhotoImage(solarrooff)

solarroof_label=Label(w2,image=solarroofff,bg="black")
solarroof_label.place(x=230,y=500)

powerwall="C:\\mohan\\tesla\\image and videos\\w22Solar Panels.jfif"
powerwalll=Image.open(powerwall)
powerwalll=powerwalll.resize((100,100))
powerwallll=ImageTk.PhotoImage(powerwalll)

powerwall_label=Label(w2,image=powerwallll,bg="black")
powerwall_label.place(x=1157, y=500)

mageback="C:\\mohan\\tesla\\image and videos\\w22magaback.jfif"
magebackk=Image.open(mageback)
magebackk=magebackk.resize((100,100))
magebackkk=ImageTk.PhotoImage(magebackk)

mageback_label=Label(w2,image=magebackkk,bg="black")
mageback_label.place(x=1207, y=180)


b1 = Button(w2, text="Solar Panels",font=('Helvetica',15), command=open_line1,bg="black", fg="white", width=10, height=1)
# Adjusted button height
b1.place(x=40, y=630)

b2 = Button(w2, text="Solar Roof",font=('Helvetica',15), command=open_line2,
            bg="black", fg="white", width=10, height=1)
b2.place(x=220, y=630)

b3 = Button(w2, text="Powerwall",font=('Helvetica',15), command=open_line3, bg="black",
            fg="white", width=10, height=1)
b3.place(x=1150, y=630)
b4 = Button(w2, text="Megapack",font=('Helvetica',15), command=open_line3, bg="black",
            fg="white", width=10, height=1)
b4.place(x=1200, y=300)

button_font = ('Helvetica', 13)
button_width = 10
button_height = 0


b5= Button(w2, text="Why Solar", command=open_line7,
            font=button_font, bg="black",fg="white", width=button_width, height=button_height)
b5.place(x=350, y=20)

b6 = Button(w2, text="Incentives", command=open_line8,
            font=button_font, bg="black",fg="white", width=button_width, height=button_height)
b6.place(x=500, y=20)

b7 = Button(w2, text="Support", command=open_line9,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b7.place(x=650, y=20)

b8 = Button(w2, text="Partner with Tesla", command=open_line10,
            font=button_font,bg="black",fg="white", width=button_width+4, height=button_height)
b8.place(x=800, y=20)



b9 = Button(w2, text="Commercial", command=open_line9,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b9.place(x=980, y=20)


b10 = Button(w2, text="Utilites", command=open_line10,
            font=button_font,bg="black",fg="white", width=button_width, height=button_height)
b10.place(x=1120, y=20)
def back():
    w2.destroy()
    import testla
b12=Button(w2,text="Back",command=back,bg="black",fg="red")
b12.place(x=1280,y=0)



def next():
    w2.destroy()
    import Charging

b13 = Button(w2, text="next", command=next, bg="black", fg="red")
b13.place(x=1323, y=0)
w2.mainloop()
