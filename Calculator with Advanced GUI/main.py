from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')


e = Entry(root, width = 65, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

one_pic = Image.open('1.png').resize((100, 100) , Image.ANTIALIAS)
one_button = ImageTk.PhotoImage(one_pic)
two_pic = Image.open('2.png').resize((100, 100) , Image.ANTIALIAS)
two_button = ImageTk.PhotoImage(two_pic)
three_pic = Image.open('3.png').resize((100, 100) , Image.ANTIALIAS)
three_button = ImageTk.PhotoImage(three_pic)
four_pic = Image.open('4.png').resize((100, 100) , Image.ANTIALIAS)
four_button = ImageTk.PhotoImage(four_pic)
five_pic = Image.open('5.png').resize((100, 100) , Image.ANTIALIAS)
five_button = ImageTk.PhotoImage(five_pic)
six_pic = Image.open('6.png').resize((100, 100) , Image.ANTIALIAS)
six_button = ImageTk.PhotoImage(six_pic)
seven_pic = Image.open('7.png').resize((100, 100) , Image.ANTIALIAS)
seven_button = ImageTk.PhotoImage(seven_pic)
eight_pic = Image.open('8.png').resize((100, 100) , Image.ANTIALIAS)
eight_button = ImageTk.PhotoImage(eight_pic)
nine_pic = Image.open('9.png').resize((100, 100) , Image.ANTIALIAS)
nine_button = ImageTk.PhotoImage(nine_pic)
zero_pic = Image.open('0.png').resize((100, 100) , Image.ANTIALIAS)
zero_button = ImageTk.PhotoImage(zero_pic)
add_pic = Image.open('+.png').resize((100, 100) , Image.ANTIALIAS)
add_button = ImageTk.PhotoImage(add_pic)
equal_pic = Image.open('=.png').resize((100, 100) , Image.ANTIALIAS)
equal_button = ImageTk.PhotoImage(equal_pic)
subtract_pic = Image.open('sub.png').resize((100, 100) , Image.ANTIALIAS)
subtract_button = ImageTk.PhotoImage(subtract_pic)
multiply_pic = Image.open('x.png').resize((100, 100) , Image.ANTIALIAS)
multiply_button = ImageTk.PhotoImage(multiply_pic)
divide_pic = Image.open('div.png').resize((100, 100) , Image.ANTIALIAS)
divide_button = ImageTk.PhotoImage(divide_pic)
clear_pic = Image.open('c.png').resize((100, 100) , Image.ANTIALIAS)
clear_button = ImageTk.PhotoImage(clear_pic)


button_1 = Button(root, image= one_button, command = lambda: button_click(1))
button_2 = Button(root, image= two_button, command = lambda: button_click(2))
button_3 = Button(root, image= three_button, command = lambda: button_click(3))
button_4 = Button(root, image= four_button, command = lambda: button_click(4))
button_5 = Button(root, image= five_button, command = lambda: button_click(5))
button_6 = Button(root, image= six_button, command = lambda: button_click(6))
button_7 = Button(root, image= seven_button, command = lambda: button_click(7))
button_8 = Button(root, image= eight_button, command = lambda: button_click(8))
button_9 = Button(root, image= nine_button, command = lambda: button_click(9))
button_0 = Button(root, image= zero_button, command = lambda: button_click(0))
button_add = Button(root, image= add_button, command = button_add)
button_equal = Button(root, image= equal_button, pady = 20, command = button_equal)
button_clear = Button(root, image= clear_button, command = button_clear)
button_subtract = Button(root, image= subtract_button, command = button_subtract)
button_multiply = Button(root, image= multiply_button, command = button_multiply)
button_divide = Button(root, image= divide_button, command = button_divide)

# button_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7,
#                button_8, button_9, button_0, button_clear, button_add, button_equal,
#                button_subtract, button_multiply, button_divide]
# row_number = 0
# column_number = 0
#
# for button in button_list:
#     Grid.rowconfigure(root, row_number, weight = 1)
#     Grid.columnconfigure(root, column_number, weight = 1)
#     row_number += 1
#     column_number += 1

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 1)
button_clear.grid(row = 4, column = 0)
button_add.grid(row = 1, column = 3)
button_equal.grid(row = 4, column = 2)
button_subtract.grid(row = 2, column = 3)
button_multiply.grid(row = 3, column = 3)
button_divide.grid(row = 4, column = 3)


root.mainloop()