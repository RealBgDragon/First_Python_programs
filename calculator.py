import tkinter as tk
import math

#! Create a new Tkinter window
window = tk.Tk()




#! chosme the window sieze
window.geometry("500x500")

# Create a label widget and add it to the window
label = tk.Label(window, text="Calculator")
label.pack()

# input
entry_widget1 = tk.Entry(window, width=30, font=("Arial", 20))
entry_widget1.place(x=25, y=50)

user_input1 = entry_widget1.get()

entry_widget2 = tk.Entry(window, width=30, font=("Arial", 20))
entry_widget2.place(x=25, y=125)

user_input2 = entry_widget2.get()

label1 = tk.Label(window, text="", width=30, font=("Arial", 20))
label1.place(x=15, y=450)

x = 0
y = 0
# add method
def add():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x + y
    label1.configure(text=str(result))
    
# add buttom
add_button = tk.Button(window, text="+", width=5, height=1, command=add)
add_button.config(font=("Arial", 20))
add_button.place(x=25, y=200)

# subtract method
def sub():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x - y
    label1.configure(text=str(result))
    
# subtract button
add_button = tk.Button(window, text="-", width=5, height=1, command=sub)
add_button.config(font=("Arial", 20))
add_button.place(x=125, y=200)

# multiply method
def mult():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x * y
    label1.configure(text=str(result))
    
# multiply buttom
add_button = tk.Button(window, text="*", width=5, height=1, command=mult)
add_button.config(font=("Arial", 20))
add_button.place(x=225, y=200)

# divide method
def div():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x / y
    result = round(result, 2)
    label1.configure(text=str(result))
    
# divide buttom
add_button = tk.Button(window, text="/", width=9, height=1, command=div)
add_button.config(font=("Arial", 20))
add_button.place(x=325, y=200)

#sqrt method
def sqrt():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x ** (1/y)
    result = round(result, 2)
    label1.configure(text=str(result))

# sqrt button
add_button = tk.Button(window, text="√", width=5, height=1, command=sqrt)
add_button.config(font=("Arial", 20))
add_button.place(x=25, y=265)

# pow method
def pow():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = x ** y
    label1.configure(text=str(result))

# pow button
add_button = tk.Button(window, text="^", width=5, height=1, command=pow)
add_button.config(font=("Arial", 20))
add_button.place(x=125, y=265)

# log method
def log():
    x = float(entry_widget1.get())
    y = float(entry_widget2.get())
    result = math.log(x) / math.log(y)
    label1.configure(text=str(result))

# log button
add_button = tk.Button(window, text="log", width=5, height=1, command=log)
add_button.config(font=("Arial", 20))
add_button.place(x=225, y=265)

# factorial

def factorial():
    x = float(entry_widget1.get())
    result = 1
    while x > 0:
        result = result * x
        x -= 1
    label1.configure(text=str(result))
        

add_button = tk.Button(window, text="n!", width=9, height=1, command=factorial)
add_button.config(font=("Arial", 20))
add_button.place(x=325, y=265)

# mile and km method
def distance():
    temp = ""
    x = entry_widget1.get()
    y = entry_widget2.get()
    if x and not y:  # if x has a value and y is empty
        x = float(x)
        result = x * 1.60934
        temp = "km"
    elif y and not x:  # if y has a value and x is empty
        y = float(y)
        result = y / 1.60934
        result = round(result, 4)
        temp = "mil"
    elif x and y:  # if both x and y have values
        x = float(x)
        y = float(y)
        result = "please input only one number"
    else:  # if both x and y are empty
        result = "No input"  
    label1.configure(text=str(result) + temp)

# mile and km button
add_button = tk.Button(window, text="mil/km", width=5, height=1, command=distance)
add_button.config(font=("Arial", 20))
add_button.place(x=25, y=330)

# pound and kg method
def weight():
    temp = ""
    x = entry_widget1.get()
    y = entry_widget2.get()
    if x and not y:  # if x has a value and y is empty
        x = float(x)
        result = x / 2.20462
        result = round(result, 4)
        temp = "kg"
    elif y and not x:  # if y has a value and x is empty
        y = float(y)
        result = y * 2.20462
        temp = "pound"
    elif x and y:  # if both x and y have values
        x = float(x)
        y = float(y)
        result = "please input only one number"
    else:  # if both x and y are empty
        result = "No input"  
    label1.configure(text=str(result) + temp)

# pound and kg button
add_button = tk.Button(window, text="pnd/kg", width=5, height=1, command=weight)
add_button.config(font=("Arial", 20))
add_button.place(x=125, y=330)

#! feet to meters
def feet_to_meters(feet):
    feet_str, inches_str = feet.split("f")
    #feet_str, inches_str = feet.split(" ")
    
    # feet to m
    feet_m = float(feet_str) * 0.3048
    
    # if there is an inches component, convert it to meters and add to the feet component
    if inches_str:
        inches_m = float(inches_str) * 0.0254
        total_m = feet_m + inches_m
    else:
        total_m = feet_m
        
    return total_m

#! meters to feet
def meters_to_feet(meters):
    total_inches = meters / 0.0254
    feet = int(total_inches // 12)
    inches = int(total_inches % 12)
    return f"{feet}'{inches}\""
    


# foot and meter method
def lenght():
    temp = ""
    x = entry_widget1.get()
    y = entry_widget2.get()
    if x and not y:  # if x has a value and y is empty
        result = feet_to_meters(x)
        result = round(result, 2)
        temp = "m"
    elif y and not x:  # if y has a value and x is empty
        y = float(y)
        result = y/100
        #result = y / 3.28084
        temp = "ft"
        result = meters_to_feet(result)
    elif x and y:  # if both x and y have values
        x = float(x)
        y = float(y)
        result = "please input only one number"
    else:  # if both x and y are empty
        result = "No input"  
    label1.configure(text=str(result) + temp)

# foot and meter button
add_button = tk.Button(window, text="foot/m", width=5, height=1, command=lenght)
add_button.config(font=("Arial", 20))
add_button.place(x=225, y=330)

def speed():
    temp = ""
    x = entry_widget1.get()
    y = entry_widget2.get()
    if x and not y:  # if x has a value and y is empty
        x = float(x)
        result = x * 1.60934
        temp = "kmph"
    elif y and not x:  # if y has a value and x is empty
        y = float(y)
        result = y / 1.60934
        result = round(result, 4)
        temp = "mph"
    elif x and y:  # if both x and y have values
        x = float(x)
        y = float(y)
        result = "please input only one number"
    else:  # if both x and y are empty
        result = "No input"  
    label1.configure(text=str(result) + temp)

# mph and kph button
add_button = tk.Button(window, text="kph/mph", width=9, height=1, command=speed)
add_button.config(font=("Arial", 20))
add_button.place(x=325, y=330)


#TODO think of other actions

# Run the Tkinter event loop
window.mainloop()