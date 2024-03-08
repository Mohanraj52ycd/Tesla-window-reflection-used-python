import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkvideo import tkvideo
from PIL import Image, ImageTk
import customtkinter
import webbrowser

w5= tk.Tk()
w5.title("ＴΞＳＬΛ")
w5.wm_state('zoomed')
w5.configure(background="black")
open=Label(w5)
open.place(x=0,y=60)
open_video=tkvideo("C:\\mohan\\tesla\\image and videos\\w5The_Official_Tesla_Shop_Tesla_1-html5-shop.tesla-1-0-sub-0.0-86400.0.mp4",open,size=(1350,650))
open_video.play()
l=Label(w5,text='ＴΞＳＬΛ',bg='black',fg='white',font=('Helvetica',25))
l.place(x=0,y=5)


iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
w5.iconphoto(False, tkicon)

def shop():
    webbrowser.open("https://shop.tesla.com//")
b1=Button(w5,text="SHOP",font=(None,13),bg="black",fg="white",command=shop)
b1.place(x=200,y=10)
def charging():
    webbrowser.open("https://shop.tesla.com//category//charging")
b2=Button(w5,text="CHARGING",font=(None,13),bg="black",fg="white",command=charging)
b2.place(x=350,y=10)

def vehicle_accessories():
    webbrowser.open("https://shop.tesla.com/category/vehicle-accessories")
b3=Button(w5,text="VEHICLE ACCESSORIES",font=(None,13),bg="black",fg="white",command=vehicle_accessories)
b3.place(x=446,y=10)

def apparel ():
    webbrowser.open("https://shop.tesla.com//category//apparel")
b4=Button(w5,text="APPAREL",font=(None,13),bg="black",fg="white",command=apparel)
b4.place(x=650,y=10)
def lifestyle ():
    webbrowser.open("https://shop.tesla.com/category/lifestyle")
b5=Button(w5,text="LIFESTYLE",font=(None,13),bg="black",fg="white",command=apparel)
b5.place(x=735,y=10)
def search_logo():
    webbrowser.open("https://shop.tesla.com//search?searchTerm=")
search_label = tk.Label(w5, text="search", font=(None, 12))
search_label.place(x=950, y=13)
search_label.bind('<Button>',lambda e:search_logo())
name_entry = tk.Entry(w5, font=(None, 13))
name_entry.place(x=1010, y=13)
def shop_image1():
    webbrowser.open("https://shop.tesla.com//cart")
shop_image="C:\\mohan\\tesla\\image and videos\\w5shop.jfif"
shop_imagee=Image.open(shop_image)
shop_imagee=shop_imagee.resize((40,40))
shop_imageee=ImageTk.PhotoImage(shop_imagee)
shop_label=Label(w5,image=shop_imageee,bg="black")
shop_label.bind("<Button-1>", lambda e: shop_image1())
shop_label.place(x=1205,y=1)

def menu ():
    webbrowser.open("https://www.tesla.com/support/menu")
b6=Button(w5,text="MENU",font=(None,13),bg="black",fg="white",command=menu)
b6.place(x=1270,y=10)
cybertruck="C:\\mohan\\tesla\\image and videos\\w5cyber.jfif"
cybertruckk=Image.open(cybertruck)
cybertruckk=cybertruckk.resize((50,50))
cybertruckkk=ImageTk.PhotoImage(cybertruckk)
cybertruk_label=Label(w5,image=cybertruckkk,bg="black")
cybertruk_label.place(x=0,y=1000)
# Create a vertical scrollbar
ll=Label(w5, text='CYBERTRCK', bg='black', fg='white', font=('CHILLER', 30))
ll.place(x=600, y=550)

def back():
    w5.destroy()
    import testla


b13=Button(w5,text="Back",command=back,bg="black",fg="red")
b13.place(x=150,y=-5)


def shopNow ():
    w5.destroy()
    import shopnow
b8=Button(w5,text="SHOW NOW",bg="black",fg="white",command=shopNow)
b8.place(x=650,y=600)
w5.mainloop()
