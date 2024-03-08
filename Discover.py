import tkinter as tk
from tkinter import messagebox, ttk,Button
from PIL import Image, ImageTk
import tkvideo as tkv
import webbrowser


def schedule_event():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_entry.get()  # Retrieve age value
    event_type = event_var.get()
    date = date_entry.get()
    time = time_entry.get()
    destination = destination_entry.get()

    messagebox.showinfo("Event Scheduled",
                        f"Thank you, {name}! Your {event_type} event on {date} at {time} to {destination} has been scheduled.")

# Create the main window
w4 = tk.Tk()
w4.title("ＴΞＳＬΛ")
w4.configure(bg="black")
style = ttk.Style()
style.theme_use("clam")
w4.wm_state('zoomed')

iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
tkicon = ImageTk.PhotoImage(iconimg)
w4.iconphoto(False, tkicon)

video_label1 = tk.Label(w4)
player1 = tkv.tkvideo("C:\\mohan\\tesla\\image and videos\\w4EN---Solar-Contracts-Tesla-App.webm", video_label1, loop=1, size=(520, 350))
player1.play()
video_label1.pack()
video_label1.place(x=850, y=48)

video_label2 = tk.Label(w4)
player2 = tkv.tkvideo("C:\\mohan\\tesla\\image and videos\w4ee.webm", video_label2, loop=1, size=(560, 300))
player2.play()
video_label2.pack()
video_label2.place(x=286, y=400)

car_image = 'C:\\mohan\\tesla\\image and videos\\w4Tesla Model 3, portrait, 1080x2160 wallpaper.jpeg'
car_imagee = Image.open(car_image)
car_imagee = car_imagee.resize((350, 350))
car_imagees = ImageTk.PhotoImage(car_imagee)

model_s_label = tk.Label(w4, image=car_imagees, bg="black")
model_s_label.place(x=400, y=0)
title_label = tk.Label(w4, text='ＴΞＳＬΛ', bg='black', fg='white', font=('Helvetica', 25))
title_label.place(x=490, y=350)


# Create and place labels and entry widgets for user input
tk.Label(w4, text="Name:", font=(None, 12)).place(x=50, y=50)
name_entry = tk.Entry(w4, font=(None, 12))
name_entry.place(x=150, y=50)

tk.Label(w4, text="Email:", font=(None, 15)).place(x=50, y=80)
email_entry = tk.Entry(w4, font=(None, 12))
email_entry.place(x=150, y=80)

tk.Label(w4, text="Phone:", font=(None, 12)).place(x=50, y=110)
phone_entry = tk.Entry(w4, font=(None, 12))
phone_entry.place(x=150, y=110)

tk.Label(w4, text="Age:", font=(None, 12)).place(x=50, y=140)  # Add label for age
age_entry = tk.Entry(w4, font=(None, 12))
age_entry.place(x=150, y=140)  # Place age entry widget

tk.Label(w4, text="Event Type:", font=(None, 12)).place(x=50, y=170)
event_var = tk.StringVar(w4)
event_var.set("Test Drive")  # Default event type
event_options = ["Test Drive", "Product Launch", "Service Appointment"]
event_menu = tk.OptionMenu(w4, event_var, *event_options)
event_menu.place(x=150, y=170)

tk.Label(w4, text="Date:", font=(None, 12)).place(x=50, y=200)
date_entry = tk.Entry(w4, font=(None, 12))
date_entry.place(x=150, y=200)

tk.Label(w4, text="Time:", font=(None, 12)).place(x=50, y=230)
time_entry = tk.Entry(w4, font=(None, 12))
time_entry.place(x=150, y=230)

tk.Label(w4, text="Destination:", font=(None, 12)).place(x=50, y=260)  # Add label for destination
destination_entry = tk.Entry(w4, font=(None, 12))
destination_entry.place(x=150, y=260)  # Place destination entry widget

# Create and place the submit button
submit_button = tk.Button(w4, text="Schedule Demo Drive", command=schedule_event, font=(None, 12))
submit_button.place(x=100, y=290)  # Adjust button position

Resources_label = tk.Label(w4, text='Resources', bg='black', fg='white', font=('Helvetica', 20))
Resources_label.place(x=50, y=450)
Location_Services_label = tk.Label(w4, text='Location Services', bg='black', fg='white', font=('Helvetica', 20))
Location_Services_label.place(x=1000, y=410)
Location_Services_label = tk.Label(w4, text='Company', bg='black', fg='white', font=('Helvetica', 20))
Location_Services_label.place(x=1050, y=550)
def open_line1():
    webbrowser.open("https://www.tesla.com/drive")
b1 = Button(w4, text="Demo Drive", font=('Helvetica', 10), command=open_line1, bg="black", fg="white", width=8, height=1)
b1.place(x=15, y=530)

def open_line2():
    webbrowser.open("https://www.tesla.com/insurance")
b2 = Button(w4, text="Insurance", font=('Helvetica', 10), command=open_line2, bg="black", fg="white", width=8, height=1)
b2.place(x=150, y=530)

def open_line3():
    webbrowser.open("https://www.tesla.com/support/videos")
b3 = Button(w4, text="Video Guides", font=('Helvetica', 10), command=open_line3, bg="black", fg="white", width=13, height=1)
b3.place(x=15, y=580)

def open_line4():
    webbrowser.open("https://www.tesla.com/customer-stories")
b4 = Button(w4, text="Customer Stories", font=('Helvetica', 10), command=open_line4, bg="black", fg="white", width=13, height=1)
b4.place(x=150, y=580)

def open_line5():
    webbrowser.open("https://www.tesla.com/charging")
b5 = Button(w4, text="Events", font=('Helvetica', 10), command=open_line5, bg="black", fg="white", width=8, height=1)
b5.place(x=83, y=630)
def open_line6():
    webbrowser.open("https://www.tesla.com//?v=2&bounds=58.16952200395186%2C-39.237305875000004%2C15.366791624768437%2C-159.295899625&zoom=4&filters=store%2Cservice%2Csupercharger%2Cdestination%20charger%2Cbodyshop%2Cparty%2Cself%20serve%20demo%20drive%2Cnacs")
b6= Button(w4, text="Find Us", font=('Helvetica', 10), command=open_line6, bg="black", fg="white", width=8, height=1)
b6.place(x=880, y=500)

def open_line7():
    webbrowser.open("https://www.tesla.com//trips")
b7 = Button(w4, text="Trip Planner", font=('Helvetica', 10), command=open_line7, bg="black", fg="white", width=9, height=1)
b7.place(x=960, y=500)

def open_line8():
    webbrowser.open("https://www.tesla.com//support//collision-support")
b8 = Button(w4, text="Find a Collision Center", font=('Helvetica', 10),
            command=open_line8, bg="black", fg="white", width=17, height=1)
b8.place(x=1050, y=500)

def open_line9():
    webbrowser.open("https://www.tesla.com//support//certified-installers")
b9 = Button(w4, text="Find a Collision Center", font=('Helvetica', 10),
            command=open_line9, bg="black", fg="white", width=17, height=1)
b9.place(x=1200, y=500)


def open_line10():
    webbrowser.open("https://www.tesla.com//about")
b10 = Button(w4, text="About", font=('Helvetica', 10),
            command=open_line10, bg="black", fg="white", width=17, height=1)
b10.place(x=870, y=600)

def open_line11():
    webbrowser.open("https://www.tesla.com//careers")
b11 = Button(w4, text="Careers", font=('Helvetica', 10),
            command=open_line11, bg="black", fg="white", width=17, height=1)
b11.place(x=1040, y=600)

def open_line12():
    webbrowser.open("https://ir.tesla.com//#quarterly-disclosure")
b12 = Button(w4, text="Investor Relations", font=('Helvetica', 10),
            command=open_line12, bg="black", fg="white", width=17, height=1)
b12.place(x=1220, y=600)



def back():
    w4.destroy()
    import testla
b13=Button(w4,text="Back",command=back,bg="black",fg="red")
b13.place(x=1280,y=0)


def next():
    w4.destroy()
    import shop

b14 = Button(w4, text="next", command=next, bg="black", fg="red")
b14.place(x=1323, y=0)




w4.mainloop()
