#day 14

#key a single value
menu = dict({"Vegan": ["ackee","plantain"],
             "Veggie":["beans","egg"]})
print(menu)
print(menu.get("Vegan"))
#list comparision

menu["Vegan"][1] = "almond"
print(menu["Vegan"])

# Dictionary Comparison
menu_1 = dict({"Meat": ["Chicken","plantain"],
             "Pesc":["fish","egg"]})
menu_2 = dict({"Vegan": ["ackee","plantain"],
             "Veggie":["beans","egg"]})
print(menu_1 == menu_2)