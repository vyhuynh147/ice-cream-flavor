import csv

class Flavors:
    def __init__(self, flavor_name, category, calories, fat_g, cholesterol_mg, carbs_g, sugars_g, protein_g, size_cup1):
        self.flavor_name = flavor_name
        self.category = category
        self.calories = calories
        self.fat_g = fat_g
        self.cholesterol_mg = cholesterol_mg
        self.carbs_g = carbs_g
        self.sugars_g = sugars_g
        self.protein_g = protein_g
        self.size_cup = size_cup1

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
    
    def __str__(self):
        return f"{self.flavor_name} - {self.category}:  {self.calories},{self.fat_g},{self.cholesterol_mg},{self.carbs_g},{self.sugars_g},{self.protein_g}. {self.size_cup}"

flavorsList = {}

with open("BenJerryNutrition.csv", mode="r") as ice_db:
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

        flavorsList[name] = Flavors(name, category, cal, fat_g, chol_mg, carb_g, sug_g, prot_g, size_cup )
        
    print(flavorsList)
