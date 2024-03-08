from tkinter import messagebox, Button
from tkinter import *
import tkinter as tk
from tkvideo import tkvideo
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser

w3 = tk.Tk()
w3.title("ＴΞＳＬΛ")
w3.wm_state("zoomed")
w3.configure(bg="black")
iconimg = Image.open("C:\\mohan\\tesla\\image and videos\\loge.png")
icon = ImageTk.PhotoImage(iconimg)
w3.iconphoto(False, icon)
label_chage = Label(w3, text="ＴΞＳＬΛ", bg="black", fg="white", font=('Helvetica', 30))
label_chage.place(x=10, y=20)
chage_lable = Label(w3, text="Charging Calculator", bg="black", fg="white", font=("Helvetica", 30))
chage_lable.place(x=550, y=100)
connecter = Label(w3, text="How much you can save with Wall Connector", bg="black", fg="white", font=("Helvetica", 20))
connecter.place(x=450, y=150)


def connecter():
    messagebox.showinfo("Gas Savings Disclaimer", """
        Gas Savings:
        We've assumed a fuel economy of 23 miles per gallon for a comparable gasoline powered car.
        We've also assumed the national average of $0.16 per kilowatt-hour for residential electricity 
        (assumed for 100% of charging) and $3.90 per gallon for gasoline.
        Tesla efficiency values are based on Model S Dual Motor All-Wheel Drive. Comparison gasoline 
        vehicles are selected based on vehicle class, seating capacity, and standard features. 
        We use the EPA estimated range standard to compare efficiency data between our cars and a comparable 
        gasoline alternative using each vehicle's combined city/highway MPG and MPGe ratings.
        Actual range may vary based on factors such as speed, weather conditions,and elevation change.""")


# Assuming w3 is your Tkinter window
connecter_button = Button(w3, text="Gas Savings Disclaimer", command=connecter, bg="black", fg="white",font=(20))
connecter_button.place(x=1010, y=160)
def option_select():
    selected_option=combobox.get()
    if "Daliy" == option_select:
        daily_option()
    elif option_select=="Monthly":
        monthly_option()
def daily_option():
    print("Daily option selected")

def monthly_option():
    print("Monthly option selected")

def option_select_your_car():
    option_select=combobox1.get()
    if Model_S==option_your_car:
        Model_S()
    elif Model_3==option_your_car:
        Model_3()
    elif Model_X==option_your_car:
        Model_X()
    elif Model_Y==option_select:
        Model_Y()
    elif Cybertruck==option_your_car:
        Cybertruck()
def Model_S():
    print("Model S")
def Model_3():
    print("Model 3")
def Model_X():
    print("Model X")
def Model_Y():
    print("Model Y")
def Cybertruck():
    print("Cybertruck")

combobox = ttk.Combobox(w3, values=["Daily", "Monthly"],font=(None,10))
combobox.set("Select Option")
combobox.bind("<<ComboboxSelected>>", option_select)
combobox.place(x=800,y=200,width=120,height=30)

chage_video=Label(w3)
chage_video.place(x=0,y=200)
play=tkvideo("C:\\mohan\\tesla\\image and videos\\w3Supercharger-Carousel-Slide-1-Desktop-NA.webm",chage_video,loop=1,size=(500,500))
play.play()

combobox1=ttk.Combobox(w3,values=["Model S",'Model 3',"Model X","Model Y","Cybertruck"],font=(None,15))
combobox1.set("Choose car models")
combobox1.bind("<<ComboboxSelected>>",option_select_your_car)
combobox1.place(x=790,y=200,width=200,height=30)


def calculate_charging_cost():
    try:
        miles_driven = float(miles_enter.get())
        electricity_cost_per_kWh = float(rate_enter.get())
        selected_option = frequency_var.get()

        if selected_option == "Daily":
            result = miles_driven * electricity_cost_per_kWh / 100
        elif selected_option == "Monthly":
            result = miles_driven * electricity_cost_per_kWh / 100 * 30

        result_label.config(text="Estimated charging cost: ${:.2f}".format(result))
    except ValueError:
        result_label.config(text="Error: Please enter valid numeric values")




# Miles Driven Entry
miles_label = tk.Label(w3, text="Miles Driven",width=10,height=0,font=(None,15))
miles_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
miles_label.place(x=790,y=250)
miles_enter = tk.Entry(w3,width=8,font=(None,15))
miles_enter.grid(row=0, column=1, padx=30, pady=15)
miles_enter.place(x=940,y=250)

# Electricity Cost per kWh Entry
rate_label = tk.Label(w3, text="Electricity Cost per kWh:",width=25,height=0,font=(None,15))
rate_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
rate_label.place(x=630,y=300)
rate_enter = tk.Entry(w3,width=15,font=(None,15))
rate_enter.grid(row=1, column=1, padx=10, pady=5)
rate_enter.place(x=940,y=300)

# Charging Frequency OptionMenu
frequency_label = tk.Label(w3, text="Charging Frequency:",width=17,height=0,font=(None,15))
frequency_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
frequency_label.place(x=720,y=350)
frequency_var = tk.StringVar()
frequency_var.set(("Daily","Monthly"))
frequency_menu = tk.OptionMenu(w3, frequency_var, "Daily", "Monthly")
frequency_menu.grid(row=2, column=1, padx=10, pady=5, sticky="w")
frequency_menu.place(x=800,y=400)
# Calculate Button
calculate_button = tk.Button(w3, text="Calculate", command=calculate_charging_cost,width=7,height=0,font=(None,13))
calculate_button.grid(row=3, columnspan=2, padx=5, pady=3)
calculate_button.place(x=950,y=400)
# Result Label
result_label = tk.Label(w3, text="",width=30,height=0,font=(None,15))
result_label.grid(row=4, columnspan=2, padx=10, pady=5)
result_label.place(x=950,y=350)

image1="C:\\mohan\\tesla\\image and videos\\w3chaging image1.jfif"
image11=Image.open(image1)
image11=image11.resize((100,100))
image111=ImageTk.PhotoImage(image11)
image1_label=Label(w3,image=image111,bg="black")
image1_label.place(x=607,y=500)


image2="C:\\mohan\\tesla\\image and videos\\w3chaging image2.jfif"
image22=Image.open(image2)
image22=image22.resize((100,100))
image22=ImageTk.PhotoImage(image22)
image2_label=Label(w3,image=image22,bg="black")
image2_label.place(x=825,y=500)

image3="C:\\mohan\\tesla\\image and videos\\w2chaging image3.png"
image33=Image.open(image3)
image33=image33.resize((150,100))
image33=ImageTk.PhotoImage(image33)
image3_label=Label(w3,image=image33,bg="black")
image3_label.place(x=1000,y=500)

def open_line1():
    webbrowser.open("https://www.tesla.com/charging")
def open_line2():
    webbrowser.open("https://www.tesla.com//home-charging")
def open_line3():
 webbrowser.open("https://www.tesla.com//supercharger")

b1 = Button(w3, text="Charging",font=('Helvetica',15), command=open_line1,bg="black", fg="white", width=10, height=1)

b1.place(x=600, y=630)
b2 = Button(w3, text="Home Charging",font=('Helvetica',15), command=open_line2,bg="black", fg="white", width=13, height=1)

b2.place(x=800, y=630)

b3 = Button(w3, text="Supercharging",font=('Helvetica',15), command=open_line3,bg="black", fg="white", width=13, height=1)

b3.place(x=1000, y=630)


def back():
    w2.destroy()
    import testla
b12=Button(w3,text="Back",command=back,bg="black",fg="red")
b12.place(x=1250,y=0)

def next():
    w3.destroy()
    import Discover
b13=Button(w3,text="next",command=next,bg="black",fg="red")
b13.place(x=1300,y=0)
w3.mainloop()

