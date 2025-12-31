import json
from pprint import pprint
with open("C:/Users/VOSTRO/OneDrive/Attachments/Desktop/data structures/menu_items.json") as f:
    data = json.load(f)
#Write a Python script to iterate through the menu data and print the name of each main menu
for mainmenu in data:
    print(mainmenu["name"])

print("-------------------------------------------------------")
#Extract and print the name of every menu item that belongs to the "Appetizers" category.
for item in data:
    if item["name"]=="Appetizers":
        for menu in item["menuItems"]:
            print(menu["name"])
print("---------------------------------------------------------------------")
#iterate through all non-alcoholic beverages and calculate their average price. The price can
#be found under customConfigs as itemPrice.
    
non_alcoholic_price=[]
for item in data:
    if item["name"]=="Beverages":
        for sub in item["subCategories"]:
            if sub["name"]=="Non Alcoholic Beverages":
                for configs in sub["menuItems"]:
                    for price in configs["customConfigs"]:
                        non_alcoholic_price.append(price["itemPrice"])
print(non_alcoholic_price)
average=sum(non_alcoholic_price)/len(non_alcoholic_price)
print(round(average,2))

print("-----------------------------------------------------------------------------------")
#Some menu items, like "Chkn Tender Bskt," come in different sizes (e.g., "SM" and "LG"). Write
#a script to find and print the name of all items that have more than one size option in their
#customConfigs

items_with_multiple_sizes = set()

for category in data:
    menu_items = category.get("menuItems") or []

    for menu in menu_items:
        configs = menu.get("customConfigs") or []

        size_names = set()

        for config in configs:
            size_name = config.get("name")
            if size_name:
                size_names.add(size_name)

        if len(size_names) > 1:
            items_with_multiple_sizes.add(menu["name"])

pprint(items_with_multiple_sizes)

print("---------------------------------------------------------------------------------------------")

    
``