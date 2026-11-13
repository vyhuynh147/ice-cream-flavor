import csv
import random
import textwrap
from turtle import *
import os

flavorsList = {}

class Flavors:
    def __init__(self, flavor_name, category, calories, fat_g, cholesterol_mg, carbs_g, sugars_g, protein_g, size_cup1, color_hex):
        self.flavor_name = flavor_name
        self.category = category
        self.calories = calories
        self.fat_g = fat_g
        self.cholesterol_mg = cholesterol_mg
        self.carbs_g = carbs_g
        self.sugars_g = sugars_g
        self.protein_g = protein_g
        self.size_cup = size_cup1
        self.color_hex = color_hex

    def flavor_name_funct(self):
        return self.flavor_name

    def category_funct(self):
        return self.category
    
    def calories_funct(self):
        return self.calories
    
    def fat_g_funct(self):
        return self.fat_g

    def cholesterol_mg_funct(self):
        return self.cholesterol_mg

    def carbs_g_funct(self):
        return self.carbs_g

    def sugars_g_funct(self):
        return self.sugars_g

    def protein_g_funct(self):
        return self.protein_g

    def size_cup_funct(self):
        return self.size_cup

    def color_hex_funct(self):
        return self.color_hex
    
    def __str__(self):
        return f"{self.flavor_name} - {self.category}:  {self.calories},{self.fat_g},{self.cholesterol_mg},{self.carbs_g},{self.sugars_g},{self.protein_g}. {self.size_cup}, {self.color_hex}"


with open(os.path.join(os.path.dirname(__file__), "BenJerryNutrition.csv"), mode="r") as ice_db:
    flavors_DB = csv.reader(ice_db)
    next(flavors_DB)
    for flavor in flavors_DB:
        name = str(flavor[0])
        cal = int(flavor[1])
        fat_g = int(flavor[2])
        chol_mg = int(flavor[3])
        carb_g = int(flavor[4])
        sug_g = int(flavor[5])
        prot_g = int(flavor[6])
        category = str(flavor[7])
        size_cup = float(flavor[8])
        color_hex = str(flavor[9])

        flavorsList[name] = Flavors(name, category, cal, fat_g, chol_mg, carb_g, sug_g, prot_g, size_cup, color_hex)

picked_flavors = random.sample(list(flavorsList.values()), k=7)


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
    for number, flavor in enumerate(picked_flavors, start=1):
        lines = textwrap.wrap(
            f"{number}. {flavor.flavor_name} ({flavor.calories} cal)",
            width=28,
        )
        for line in lines:
            penup()
            goto(-340.25, y)
            write(line, align="center", font=("Comic Sans MS", 10, "bold"))
            y -= 15
        y -= max(0, 27 - (len(lines) - 1) * 15)
    begining()

def write_title():
    color("#ffffff")
    goto(0, 300)
    write("Kandhyce Ice Cream Special!", align="center", font=("Comic Sans MS",32, "bold"))
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

def ice_scoop(flavor, y):
    penup()
    goto(0, y)
    pendown()
    color(flavor.color_hex)
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
    choices = []
    while len(choices) < 4:
        choose = textinput(
            "Choose a flavor",
            f"Enter a menu number (1-7) or flavor name for choice {len(choices) + 1}. Leave blank to finish.",
        )
        if not choose:
            break
        choose = choose.strip()
        if choose.isdigit() and 1 <= int(choose) <= len(picked_flavors):
            choices.append(picked_flavors[int(choose) - 1])
            continue
        flavor = next(
            (item for item in picked_flavors if item.flavor_name.casefold() == choose.casefold()),
            None,
        )
        if flavor is not None:
            choices.append(flavor)

    y = -200
    for flavor in choices:
        ice_scoop(flavor, y)
        y += 70
    total_calories = sum(flavor.calories for flavor in choices)
    color("#000000")
    penup()
    goto(200, -330)
    write(f"Total calories: {total_calories}", align="center", font=("Comic Sans MS", 16, "bold"))
    print(f"Your selected flavors total {total_calories} calories.")
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

if __name__ == "__main__":
    ice_cream_order()