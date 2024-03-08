import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
from tkinter import Label,Button
shop_now = tk.Tk()
shop_now.title("ＴΞＳＬΛ")
shop_now.wm_state("zoomed")
shop_now.configure(background="black")
label_chage = Label(shop_now, text="ＴΞＳＬΛ", bg="black", fg="red", font=('Helvetica', 30))
label_chage.place(x=500, y=20)
iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
shop_now.iconphoto(False, tkicon)

CYBERTRUCK = tk.Label(shop_now, text="CYBERTRUCK", font=(None, 15), bg="black", fg="white")
CYBERTRUCK.pack(anchor='nw', padx=20, pady=10)

FEATURED_PRODUCTS = tk.Label(shop_now, text="FEATURED PRODUCTS", font=(None, 15), bg="black", fg="white")
FEATURED_PRODUCTS.pack(anchor='nw', padx=20, pady=10)

def open_link1(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-basecamp//')

CYBERTRUCK_BASECAMP_image_path1 = "C:\\mohan\\tesla\\image and videos\\shopnowimge1CYBERTRUCK BASECAMP.webp"
CYBERTRUCK_BASECAMP_image1 = Image.open(CYBERTRUCK_BASECAMP_image_path1)
CYBERTRUCK_BASECAMP_image1 = CYBERTRUCK_BASECAMP_image1.resize((200, 100))
CYBERTRUCK_BASECAMP_image_photo1 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image1)

CYBERTRUCK_BASECAMP_label1 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo1, bg="black")
CYBERTRUCK_BASECAMP_label1.bind("<Button-1>", open_link1)
CYBERTRUCK_BASECAMP_label1.place(x=30,y=100)

CYBERTRUCK_BASECAMP_text1 = tk.Label(shop_now, text="CYBERTRUCK BASECAMP", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text1.place(x=30,y=210)

CYBERTRUCK_BASECAMP_text11 = tk.Label(shop_now, text="$2,975",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text11.place(x=30,y=240)


def open_link2(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-color-paint-film?sku=2049765-00-A')


CYBERTRUCK_BASECAMP_image_path2 = "C:\\mohan\\tesla\\image and videos\\shopnowimge1.png"
CYBERTRUCK_BASECAMP_image2 = Image.open(CYBERTRUCK_BASECAMP_image_path2)
CYBERTRUCK_BASECAMP_image2 = CYBERTRUCK_BASECAMP_image2.resize((200, 200))
CYBERTRUCK_BASECAMP_image_photo2 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image2)

CYBERTRUCK_BASECAMP_label2 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo2, bg="black")
CYBERTRUCK_BASECAMP_label2.bind("<Button-1>", open_link2)
CYBERTRUCK_BASECAMP_label2.place(x=300,y=50)
CYBERTRUCK_BASECAMP_text2 = tk.Label(shop_now, text="CYBERTRUCK COLOR PAINT FILM", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text2.place(x=300,y=220)

CYBERTRUCK_BASECAMP_text22 = tk.Label(shop_now, text="$6,000",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text22.place(x=300,y=250)




def open_link3(event):
    webbrowser.open('https://shop.tesla.com//roduct//cybertruck-underseat-storage-bin')


CYBERTRUCK_BASECAMP_image_path3 = "C:\\mohan\\tesla\\image and videos\\shopnowimge3.png"
CYBERTRUCK_BASECAMP_image3 = Image.open(CYBERTRUCK_BASECAMP_image_path3)
CYBERTRUCK_BASECAMP_image3 = CYBERTRUCK_BASECAMP_image3.resize((200, 200))
CYBERTRUCK_BASECAMP_image_photo3 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image3)

CYBERTRUCK_BASECAMP_label3 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo3, bg="black")
CYBERTRUCK_BASECAMP_label3.bind("<Button-1>", open_link3)
CYBERTRUCK_BASECAMP_label3.place(x=700,y=50)
CYBERTRUCK_BASECAMP_text3 = tk.Label(shop_now, text="CYBERTRUCK UNDERSEAT STORAGE BIN", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text3.place(x=600,y=220)

CYBERTRUCK_BASECAMP_text33 = tk.Label(shop_now, text="$250",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text33.place(x=700,y=250)




def open_link4(event):
    webbrowser.open('https://shop.tesla.com//product/cybertruck-all-weather-interior-liners')


CYBERTRUCK_BASECAMP_image_path4 = "C:\\mohan\\tesla\\image and videos\\shopnowimge4.jpg"
CYBERTRUCK_BASECAMP_image4 = Image.open(CYBERTRUCK_BASECAMP_image_path4)
CYBERTRUCK_BASECAMP_image4 = CYBERTRUCK_BASECAMP_image4.resize((150, 150))
CYBERTRUCK_BASECAMP_image_photo4 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image4)

CYBERTRUCK_BASECAMP_label4 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo4, bg="black")
CYBERTRUCK_BASECAMP_label4.bind("<Button-1>", open_link4)
CYBERTRUCK_BASECAMP_label4.place(x=1150,y=60)
CYBERTRUCK_BASECAMP_text4 = tk.Label(shop_now, text="CYBERTRUCK ALL-WEATHER INTERIOR LINERS", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text4.place(x=980,y=220)

CYBERTRUCK_BASECAMP_text44 = tk.Label(shop_now, text="$295",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text44.place(x=1150,y=250)





iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
shop_now.iconphoto(False, tkicon)

def open_link5(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-carpet-interior-mats')

CYBERTRUCK_BASECAMP_image_path5 = "C:\\mohan\\tesla\\image and videos\\shopnowimge5.jpg"
CYBERTRUCK_BASECAMP_image5 = Image.open(CYBERTRUCK_BASECAMP_image_path5)
CYBERTRUCK_BASECAMP_image5 = CYBERTRUCK_BASECAMP_image5.resize((200, 100))
CYBERTRUCK_BASECAMP_image_photo5 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image5)

CYBERTRUCK_BASECAMP_label5 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo5, bg="black")
CYBERTRUCK_BASECAMP_label5.bind("<Button-1>", open_link5)
CYBERTRUCK_BASECAMP_label5.place(x=30,y=300)

CYBERTRUCK_BASECAMP_text5 = tk.Label(shop_now, text="CYBERTRUCK CARPET INTERIOR MATS", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text5.place(x=30,y=410)

CYBERTRUCK_BASECAMP_text55 = tk.Label(shop_now, text="$155",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text55.place(x=30,y=440)





def open_link6(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-glass-roof-sunshade')


CYBERTRUCK_BASECAMP_image_path6 = "C:\\mohan\\tesla\image and videos\\shopnowimge6.jpg"
CYBERTRUCK_BASECAMP_image6 = Image.open(CYBERTRUCK_BASECAMP_image_path6)
CYBERTRUCK_BASECAMP_image6 = CYBERTRUCK_BASECAMP_image6.resize((150, 150))
CYBERTRUCK_BASECAMP_image_photo6 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image6)

CYBERTRUCK_BASECAMP_label6 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo6, bg="black")
CYBERTRUCK_BASECAMP_label6.bind("<Button-1>", open_link6)
CYBERTRUCK_BASECAMP_label6.place(x=350,y=280)
CYBERTRUCK_BASECAMP_text6 = tk.Label(shop_now, text="CYBERTRUCK GLASS ROOF SUNSHADE", font=(None, 11),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text6.place(x=300,y=450)

CYBERTRUCK_BASECAMP_text66 = tk.Label(shop_now, text="$115",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text66.place(x=300,y=470)

def open_link7(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-center-console-tray')


CYBERTRUCK_BASECAMP_image_path7 = "C:\\mohan\\tesla\\image and videos\\shopnowimge7.webp"
CYBERTRUCK_BASECAMP_image7 = Image.open(CYBERTRUCK_BASECAMP_image_path7)
CYBERTRUCK_BASECAMP_image7 = CYBERTRUCK_BASECAMP_image7.resize((200, 150))
CYBERTRUCK_BASECAMP_image_photo7 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image7)

CYBERTRUCK_BASECAMP_label7 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo7, bg="black")
CYBERTRUCK_BASECAMP_label7.bind("<Button-1>", open_link7)
CYBERTRUCK_BASECAMP_label7.place(x=650,y=280)
CYBERTRUCK_BASECAMP_text7 = tk.Label(shop_now, text="CYBERTRUCK CENTER CONSOLE TRAY", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text7.place(x=600,y=450)

CYBERTRUCK_BASECAMP_text77 = tk.Label(shop_now, text="$40",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text77.place(x=700,y=470)


def open_link8(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-crossbars')


CYBERTRUCK_BASECAMP_image_path8= "C:\\mohan\\tesla\\image and videos\\shopnowimge8jpg"
CYBERTRUCK_BASECAMP_image8 = Image.open(CYBERTRUCK_BASECAMP_image_path8)
CYBERTRUCK_BASECAMP_image8 = CYBERTRUCK_BASECAMP_image8.resize((200, 150))
CYBERTRUCK_BASECAMP_image_photo8 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image8)

CYBERTRUCK_BASECAMP_label8 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo8, bg="black")
CYBERTRUCK_BASECAMP_label8.bind("<Button-1>", open_link8)
CYBERTRUCK_BASECAMP_label8.place(x=1030,y=280)
CYBERTRUCK_BASECAMP_text8 = tk.Label(shop_now, text="CYBERTRUCK CROSSBARS", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text8.place(x=1030,y=450)

CYBERTRUCK_BASECAMP_text88 = tk.Label(shop_now, text="$800",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text88.place(x=1150,y=470)


def open_link9(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-tailgate-ramp')

CYBERTRUCK_BASECAMP_image_path9 = "C:\\mohan\\tesla\\image and videos\\shopnowimge9.jpg"
CYBERTRUCK_BASECAMP_image9 = Image.open(CYBERTRUCK_BASECAMP_image_path9)
CYBERTRUCK_BASECAMP_image9 = CYBERTRUCK_BASECAMP_image9.resize((200, 100))
CYBERTRUCK_BASECAMP_image_photo9 = ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image9)

CYBERTRUCK_BASECAMP_label9 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo9, bg="black")
CYBERTRUCK_BASECAMP_label9.bind("<Button-1>", open_link9)
CYBERTRUCK_BASECAMP_label9.place(x=30,y=500)

CYBERTRUCK_BASECAMP_text9 = tk.Label(shop_now, text="CYBERTRUCK TAILGATE RAMP", font=(None, 12),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text9.place(x=30,y=620)

CYBERTRUCK_BASECAMP_text99 = tk.Label(shop_now, text="$400",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text99.place(x=30,y=640)



def open_link10(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-bumper-protectors')


CYBERTRUCK_BASECAMP_image_path10 = "C:\\mohan\\tesla\\image and videos\\shopnowimge10.jpg"
CYBERTRUCK_BASECAMP_image10 = Image.open(CYBERTRUCK_BASECAMP_image_path10)
CYBERTRUCK_BASECAMP_image10 = CYBERTRUCK_BASECAMP_image10.resize((150, 100))
CYBERTRUCK_BASECAMP_image_photo10= ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image10)

CYBERTRUCK_BASECAMP_label10 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo10, bg="black")
CYBERTRUCK_BASECAMP_label10.bind("<Button-1>", open_link10)
CYBERTRUCK_BASECAMP_label10.place(x=350,y=500)
CYBERTRUCK_BASECAMP_text10 = tk.Label(shop_now, text="CYBERTRUCK BUMPER PROTECTORS", font=(None, 11),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text10.place(x=300,y=620)

CYBERTRUCK_BASECAMP_text10 = tk.Label(shop_now, text="$80",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text10.place(x=300,y=650)




def open_link11(event):
    webbrowser.open('https://shop.tesla.com//category//vehicle-accessories//cybertruck')


CYBERTRUCK_BASECAMP_image_path11 = "C:\\mohan\\tesla\\image and videos\\shopnowimge11.jpg"
CYBERTRUCK_BASECAMP_image11 = Image.open(CYBERTRUCK_BASECAMP_image_path11)
CYBERTRUCK_BASECAMP_image11 = CYBERTRUCK_BASECAMP_image11.resize((200, 100))
CYBERTRUCK_BASECAMP_image_photo11= ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image11)

CYBERTRUCK_BASECAMP_label11 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo11, bg="black")
CYBERTRUCK_BASECAMP_label11.bind("<Button-1>", open_link11)
CYBERTRUCK_BASECAMP_label11.place(x=700,y=500)
CYBERTRUCK_BASECAMP_text11 = tk.Label(shop_now, text="CYBERTRUCK OMFG DECAL", font=(None, 11),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text11.place(x=700,y=620)

CYBERTRUCK_BASECAMP_text11 = tk.Label(shop_now, text="$55",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text11.place(x=700,y=650)







def open_link12(event):
    webbrowser.open('https://shop.tesla.com//product//cybertruck-20_-snow-chains')


CYBERTRUCK_BASECAMP_image_path12 = "C:\\mohan\\tesla\\image and videos\\shopnowimge12.jpg"
CYBERTRUCK_BASECAMP_image12 = Image.open(CYBERTRUCK_BASECAMP_image_path12)
CYBERTRUCK_BASECAMP_image12 = CYBERTRUCK_BASECAMP_image12.resize((200, 100))
CYBERTRUCK_BASECAMP_image_photo12= ImageTk.PhotoImage(CYBERTRUCK_BASECAMP_image12)

CYBERTRUCK_BASECAMP_label12 = tk.Label(shop_now, image=CYBERTRUCK_BASECAMP_image_photo12, bg="black")
CYBERTRUCK_BASECAMP_label12.bind("<Button-1>", open_link12)
CYBERTRUCK_BASECAMP_label12.place(x=1100,y=500)
CYBERTRUCK_BASECAMP_text12 = tk.Label(shop_now, text="CYBERTRUCK 20 SNOW CHAINS", font=(None, 11),
                                     bg="black", fg="white")
CYBERTRUCK_BASECAMP_text12.place(x=1100,y=620)

CYBERTRUCK_BASECAMP_text12 = tk.Label(shop_now, text="$345",
                                     font=(None, 12), bg="black", fg="white")
CYBERTRUCK_BASECAMP_text12.place(x=1100,y=650)

def back():
    shop_now.destroy()
    import testla


b13=Button(shop_now,text="Back",command=back,bg="black",fg="red")
b13.place(x=1350,y=0)





shop_now.mainloop()
