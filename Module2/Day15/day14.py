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
#keys and values (iterative printing out)
print(menu_1.keys())
print(menu_1.values())
for k in menu_1.keys():
    print(k)
for v in menu_1.values():
    print(v)
for i in menu_1.items():
    print(i)
#order (this could be probably be used to change the relationship with the data )
ordered_keys = list(menu_1.keys())
print(ordered_keys)
ordered_keys.sort(reverse=True)
print(ordered_keys)
#tuple
menu_tuple = tuple(menu.items())
print(menu_tuple)
print(type(menu_tuple))
print(menu_tuple[0])
print(type(menu_tuple[0]))
#tuple obtain key value
print(menu_tuple[0][0])
print(type(menu_tuple[0][0]))
# Slicing the key/value tuple to obtain the value.
print(menu_tuple[0][1])
print(type(menu_tuple[0][1]))
# Slicing the second item in the value list.
print(menu_tuple[0][1][1])
print(type(menu_tuple[0][1][1]))
# Instead of implementing triple slicing to get some spam, let's use the dictionary to obtain the same result.
print(menu["Vegan"][1])
print(menu_tuple[0][1][1] == menu["Vegan"][1])

# The `get()` method is a way to retrieve a value from a key, but also contain a default value if no key is found.
order = input("what would you like to order ?")
if menu.get(order, 0) == 0:
    print("{} is not a valid dish. Please try again.".format(order))
else:
    print("{} contains {}".format(order, menu.get(order)))


# The `setdefault()` method is used to create a default key/value combination for a dictionary. This is useful for
# applications where verbose data is required, but all of the information is not available. If the dictionary already
# contains a key by the default's name, the value is not changed by the default.
transportation = {"name": "coconut", "color": "brown"}
print(transportation.items())
transportation.setdefault("received_by", "swa")
print(transportation.items())
transportation.setdefault("received_by", "swallow")
print(transportation.items())