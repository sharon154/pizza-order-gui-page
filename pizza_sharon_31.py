from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox



# Create a new window
root = Tk()
root.title("Pizza Application")
root.geometry("1200x920")

def submit_order():
    # Retrieve user inputs from tkinter variables
    size = int(size_var.get())
    crust = crust_var.get()
    topping = toppings_var.get()
    flavor = flavors_var.get()
    name = name_entry.get()
    address = address_entry.get()
    contact = contact_entry.get()
    cost=total_price2.cget("text")
    # Create a new window for the order confirmation page
    order_confirmation_window = Toplevel(root)
    order_confirmation_window.title("Order Confirmation")
    order_confirmation_window.geometry("450x500")
    order_confirmation_window.configure(background="lightyellow")


    # Add widgets to display the order information
    Label(order_confirmation_window, text="Order Summary", font=("Times 20 italic bold"),bd=10,bg="maroon",fg="lightyellow",relief=RIDGE).pack(fill=X)
    Label(order_confirmation_window, text=f"Name: {name}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Address: {address}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Contact: {contact}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Size: {size}-inch",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Crust: {crust}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Flavor: {flavor}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Toppings: {topping}",font="fixedsys 15",bg="lightyellow").pack(pady=5)
    Label(order_confirmation_window, text=f"Total Cost: {cost}",font="fixedsys 15",bg="lightyellow").pack(pady=5)


    Button(order_confirmation_window, text="OK",font=("Times 10 italic bold"),bg="lightgreen",command=order_confirmation_window.destroy).pack(pady=10)

# Create a frame for the header label
header_frame = Frame(root, bg="maroon", bd=20, pady=5, relief="sunken")
header_frame.pack(side=TOP, fill=X)

# Create the header label
header_label = Label(header_frame,text='The Pizza Block', font=('times', 60, 'bold','italic'), bd=20,bg='light yellow', fg='maroon', justify=CENTER)
header_label.pack(fill=X)

#BGIMAGE
canvas = Canvas(root, width=1200, height=820)
canvas.pack()

bg_photo = PhotoImage(file="pizza_bgimage2.png")

canvas.create_image(0, 0, anchor=NW, image=bg_photo)

# Create a label to display the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=180)

size_frame = LabelFrame(root, text="Select Pizza Size",font="Times 20 italic bold", fg='white', bg='maroon', borderwidth=3, relief="sunken")
size_frame.place(x=370,y=220)

# Create a tkinter variable to store the selected size
size_var = StringVar()

small_radio = Radiobutton(size_frame, text="Small (10\")", variable=size_var, value="10",bg="light yellow",font="fixedsys 15")
small_radio.grid(row=1, column=1,pady=7)

medium_radio = Radiobutton(size_frame, text="Medium (12\")", variable=size_var, value="12",bg="light yellow",font="fixedsys 15")
medium_radio.grid(row=2, column=1, padx=10, pady=7)

large_radio = Radiobutton(size_frame, text="Large (14\")", variable=size_var, value="14",bg="light yellow",font="fixedsys 15")
large_radio.grid(row=3, column=1, padx=10, pady=7)

# Set the default value for the size variable
size_var.set("12")


# Create a frame for selecting crust
crust_frame = LabelFrame(root, text="Select Pizza Crust",font="Times 20 italic bold", fg='white', bg='maroon', borderwidth=3, relief="sunken")
crust_frame.place(x=80, y=220)

# Create a tkinter variable to store the selected crust
crust_var = StringVar()

# Create radio buttons for crust options
thin_radio = Radiobutton(crust_frame, text="Thin", variable=crust_var, value="Thin", bg="light yellow", font="fixedsys 15")
thin_radio.grid(row=0,column=0,padx=20)

thin_price=Label(crust_frame,text="Rs250",font="fixedsys 15")
thin_price.grid(row=0,column=1)

# Set the default value for the crust variable
crust_var.set("Thin")

thick_radio = Radiobutton(crust_frame, text="Thick", variable=crust_var, value="Thick", bg="light yellow", font="fixedsys 15")
thick_radio.grid(row=1,column=0,pady=10)

thick_price=Label(crust_frame,text="Rs320",font="fixedsys 15")
thick_price.grid(row=1,column=1)

crust_prices = {
    "Thin":250,
    "Thick":310
}

crust_price1 = Label(crust_frame, text=f"Price:", font="fixedsys 15")
crust_price1.grid(row=2, column=0,pady=15)

crust_price2 = Label(crust_frame, text=f"Rs{crust_prices[crust_var.get()]}", font="fixedsys 15")
crust_price2.grid(row=2, column=1)




#toppings

toppings_frame = LabelFrame(root, text="Select Pizza Toppings", font="Times 20 italic bold", fg='white', bg='maroon', borderwidth=3, relief="sunken")
toppings_frame.place(x=80, y=410)

toppings_var = StringVar()

pepperoni_cb = Checkbutton(toppings_frame, text="Pepperoni", variable=toppings_var, onvalue="Pepperoni", offvalue="", bg="light yellow", font="fixedsys 15")
pepperoni_cb.grid(row=0,column=0,padx=10,pady=5)

pepperoni_price = Label(toppings_frame, text="Rs35", font="fixedsys 15")
pepperoni_price.grid(row=0, column=1, padx=10, pady=5)

mushroom_cb = Checkbutton(toppings_frame, text="Mushroom", variable=toppings_var, onvalue="Mushroom", offvalue="Pepperoni", bg="light yellow", font="fixedsys 15")
mushroom_cb.grid(row=1, column=0, padx=10, pady=5)

mushroom_price = Label(toppings_frame, text="Rs25", font="fixedsys 15")
mushroom_price.grid(row=1, column=1, padx=10, pady=5)

cheese_cb = Checkbutton(toppings_frame, text="Extra Cheese", variable=toppings_var, onvalue="Extra Cheese", offvalue="", bg="light yellow", font="fixedsys 15")
cheese_cb.grid(row=2, column=0, padx=10, pady=5)

cheese_price = Label(toppings_frame, text="Rs20", font="fixedsys 15")
cheese_price.grid(row=2, column=1, padx=10, pady=5)

blackolive_cb = Checkbutton(toppings_frame, text="Black Olives", variable=toppings_var, onvalue="Black Olives", offvalue="", bg="light yellow", font="fixedsys 15")
blackolive_cb.grid(row=3, column=0, padx=10, pady=5)

blackolive_price = Label(toppings_frame, text="Rs30", font="fixedsys 15")
blackolive_price.grid(row=3, column=1, padx=10, pady=5)

onions_cb = Checkbutton(toppings_frame, text="Onions", variable=toppings_var, onvalue="Onions", offvalue="", bg="light yellow", font="fixedsys 15")
onions_cb.grid(row=4, column=0, padx=10, pady=5)

onions_price = Label(toppings_frame, text="Rs15", font="fixedsys 15")
onions_price.grid(row=4, column=1, padx=10, pady=5)

sausage_cb = Checkbutton(toppings_frame, text="Sausage", variable=toppings_var, onvalue="Sausage", offvalue="", bg="light yellow", font="fixedsys 15")
sausage_cb.grid(row=5, column=0, padx=10, pady=5)

sausage_price = Label(toppings_frame, text="Rs40", font="fixedsys 15")
sausage_price.grid(row=5, column=1, padx=10, pady=5)

toppings_var.set("Pepperoni")

toppings_prices = {
    "Pepperoni":35,
    "Mushroom":25,
    "Extra Cheese":20,
    "Black Olives":30,
    "Onions":15,
    "Sausage":40
}

toppings_price1 = Label(toppings_frame, text=f"Price:", font="fixedsys 15")
toppings_price1.grid(row=6, column=0,pady=30)

toppings_price2 = Label(toppings_frame, text=f"Rs{toppings_prices[toppings_var.get()]}", font="fixedsys 15")
toppings_price2.grid(row=6, column=1)


#Flavours

flavors_frame = LabelFrame(root, text="Select Pizza Flavors", font="Times 20 italic bold", fg='white', bg='maroon', borderwidth=3, relief="sunken")
flavors_frame.place(x=370, y=410)

flavors_var = StringVar()

cheesencorn_flavor_rb = Radiobutton(flavors_frame, text="Cheese n Corn", variable=flavors_var,value="Cheese n Corn",bg="light yellow", font="fixedsys 15")
cheesencorn_flavor_rb.grid(row=0, column=0, padx=10, pady=5)

cheesencorn_price=Label(flavors_frame,text="Rs 89.99",font="fixedsys 15")
cheesencorn_price.grid(row=0, column=1, padx=10, pady=5)

margherita_flavor_rb = Radiobutton(flavors_frame, text="Margherita", variable=flavors_var,value="Margherita",bg="light yellow", font="fixedsys 15")
margherita_flavor_rb.grid(row=1, column=0, padx=10, pady=5)

margherita_price=Label(flavors_frame,text="Rs 59.99",font="fixedsys 15")
margherita_price.grid(row=1, column=1, padx=10, pady=5)

hawaiian_flavor_rb = Radiobutton(flavors_frame, text="Hawaiian", variable=flavors_var,value="Hawaiian",bg="light yellow", font="fixedsys 15")
hawaiian_flavor_rb.grid(row=2, column=0, padx=10, pady=5)

hawaiian_price=Label(flavors_frame,text="Rs 79.99",font="fixedsys 15")
hawaiian_price.grid(row=2, column=1, padx=10, pady=5)

meat_lovers_flavor_rb = Radiobutton(flavors_frame, text="Meat Lovers", variable=flavors_var,value="Meat Lovers",bg="light yellow", font="fixedsys 15")
meat_lovers_flavor_rb.grid(row=3, column=0, padx=10, pady=5)

meat_lovers_price=Label(flavors_frame,text="Rs 119.99",font="fixedsys 15")
meat_lovers_price.grid(row=3, column=1, padx=10, pady=5)

veggie_lovers_flavor_rb = Radiobutton(flavors_frame, text="Veggie Lovers", variable=flavors_var,value="Veggie Lovers",bg="light yellow", font="fixedsys 15")
veggie_lovers_flavor_rb.grid(row=4, column=0, padx=10, pady=5)

veggie_lovers_price=Label(flavors_frame,text="Rs 69.99",font="fixedsys 15")
veggie_lovers_price.grid(row=4, column=1, padx=10, pady=5)

bbq_chicken_flavor_rb = Radiobutton(flavors_frame, text="BBQ Chicken", variable=flavors_var,value="BBQ Chicken", bg="light yellow", font="fixedsys 15")
bbq_chicken_flavor_rb.grid(row=5, column=0, padx=10, pady=5)

bbq_chicken_price=Label(flavors_frame,text="Rs 139.99",font="fixedsys 15")
bbq_chicken_price.grid(row=5, column=1, padx=10, pady=5)

flavors_var.set("Cheese n Corn")

flavors_prices = {
    "Cheese n Corn": 89.99,
    "Margherita": 59.99,
    "Hawaiian": 79.99,
    "Meat Lovers": 119.99,
    "Veggie Lovers": 69.99,
    "BBQ Chicken": 139.99
}

flavors_price1 = Label(flavors_frame, text=f"Price:", font="fixedsys 15")
flavors_price1.grid(row=6, column=0,pady=30)

flavors_price2 = Label(flavors_frame, text=f"Rs{flavors_prices[flavors_var.get()]:.2f}", font="fixedsys 15")
flavors_price2.grid(row=6, column=1)


def update_price():
    crust_price2.config(text=f"Rs{crust_prices[crust_var.get()]}")
    
    toppings_price2.config(text=f"Rs{toppings_prices[toppings_var.get()]}")

    flavors_price2.config(text=f"Rs{flavors_prices[flavors_var.get()]:.2f}")

    calculate_total_price()

def calculate_total_price():
    crust_price = crust_prices[crust_var.get()]
    toppings_price = toppings_prices[toppings_var.get()]
    flavors_price = flavors_prices[flavors_var.get()]
    total_price = crust_price + toppings_price + flavors_price
    total_price2.config(text=f"Rs{total_price:.2f}")

crust_var.trace("w", lambda *args: update_price())

toppings_var.trace("w", lambda *args: update_price())
    
flavors_var.trace("w", lambda *args: update_price())




#NAME ADDRESS CONTACT 
info_frame = LabelFrame(root, text="Enter Your Information",font="Times 20 italic bold",fg="white",bg="maroon",borderwidth=3,relief="sunken")
info_frame.place(x=850,y=220)

name_label = Label(info_frame, text="Name:",font="fixedsys 15",bg="light yellow")
name_label.grid(row=0, column=0, pady=10)
name_entry = Entry(info_frame,bg="light yellow")
name_entry.grid(row=0, column=1, padx=5)

address_label = Label(info_frame, text="Address:",font="fixedsys 15",bg="light yellow")
address_label.grid(row=1, column=0,pady=10)
address_entry = Entry(info_frame,bg="light yellow")
address_entry.grid(row=1, column=1, padx=5)

contact_label=Label(info_frame, text="Contact no:",font="fixedsys 15",bg="light yellow")
contact_label.grid(row=2, column=0,pady=10)
contact_entry = Entry(info_frame,bg="light yellow")
contact_entry.grid(row=2, column=1, padx=5)

total_price_label=Label(info_frame, text="Total Price:",font="fixedsys 15",bg="light yellow")
total_price_label.grid(row=3, column=0,pady=10)
total_price2= Label(info_frame,font="fixedsys 15")
total_price2.grid(row=3, column=1, padx=5)

#contact
contact=Label(root,text="For queries contact: 4444 444 444 \n EMAIL: thepizzablockvadodara@gmail.com",fg="light yellow",font="Times 12 italic bold",bg="maroon").place(x=870,y=700)

# Create a button to submit the order

submit_button = Button(info_frame, text="Submit Order",fg="black",bg="light green",font="fixedsys 15 bold",bd=10,relief="groove", command=submit_order)
submit_button.grid(row=4,column=1,padx=15,pady=30)

# Start the main event loop
root.mainloop()

