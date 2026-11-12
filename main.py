from turtle import *
from collections import deque
import os

flavors = {
        "chocolate": "#663B2A",
        "vanilla": "#d2a679",
        "mint": "#66ffcc",
        "strawberry": "#ff4d4d",
        "banana": "#EBD35F",
        "coffee": "#A15A36",
        "bubble gum": "#CC65AF"
    }

def clear_Terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def begining():
    penup()
    color("#000000")
    home()

def set_Up():
    # set up
    clear_Terminal()
    screen = Screen()
    screen.setup(width=962, height=850)
    bgcolor("#f25a5a")
    pensize(2.5)
    speed(0)
    hideturtle()
    begining()

def draw_Lines():
    color("#972121")
    x =481
    penup()
    right(90)
    goto(x,425)
    for i in range(7):
        pendown()
        forward(850)
        penup()
        x-=137.428571429
        goto(x, 425)
    begining()

def flavor_Menu():
    penup()
    color("#000000")
    goto(-220.5, 176.5)
    pendown()
    begin_fill()
    for i in range(2):
        right(90)
        forward(425)
        right(90)
        forward(240.5)
    color("#ffffff")
    end_fill()
    begining()

def write_Flavor():
    color("#CE0303")
    y=135
    goto(-340.25,y)
    for word in flavors:
        write(word, align="center", font=("Comic Sans MS", 14, "bold"))
        y -= 60
        goto(-340.25, y)
    begining()

def write_title():
    color("#ffffff")
    goto(0, 300)
    write("Gibby's Ice Cream Special!", align="center", font=("Comic Sans MS",32, "bold"))
    begining()

def ice_cone():
    penup()
    goto(60, -176)
    color("#E0C5A1")
    pendown()

    begin_fill()
    for i in range(3):
        right(120)
        forward(120)
    end_fill()
    begining()

def ice_scoop(choice, y):
    penup()
    goto(0, y)
    pendown()
    color(flavors[choice])
    begin_fill()
    circle(60)
    end_fill()
    x_pos = [-45, 0, 45]
    for x in x_pos:
        penup()
        goto(x, y - 10)
        pendown()
        begin_fill()
        circle(20)
        end_fill()

def pick_Flavor():
    choices = deque(maxlen=4)
    while len(choices) < 4:
        choose = textinput("Choose a flavor",f"Enter Flavor number {len(choices) + 1} or cancel to finish")
        if not choose:
            break
        if choose in flavors:
            choices.append(choose.strip().lower())
        else:
            continue
    y = -200
    for choice in choices:
        ice_scoop(choice, y)
        y += 70
    begining()

def ice_cream_order():
    set_Up()
    draw_Lines()
    write_title()
    flavor_Menu()
    write_Flavor()
    ice_cone()
    pick_Flavor()
    done()

ice_cream_order()