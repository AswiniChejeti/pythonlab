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

#5. List All Wing Flavors
#The "Chicken Wings" item has several flavor options. Extract and print the name of each
#"Wing Flavor" available.
    
for catgory in data:
    catgory=catgory.get("menuItems") or []
    for item in catgory:
        if item["name"]=="Chicken Wings":
            for configs in item["customConfigs"]:
                for m in configs["mandatoryModifiers"]:
                     if m["name"]=="Wing Flavor":
                        for  modifiers in m["modifiers"]:
                            print(modifiers["name"])

print("-----------------------------------------------------------------------------------------------")


#6. Identify Items with Mandatory ModifiersSome menu items require the customer to make a choice (e.g., a dipping sauce). 
#Find andprint the name of all menu items that have at least one mandatory modifier.
items_opt=set()
for catgory in data:
    menuItems=catgory.get("menuItems") or []
    for menu in menuItems:
        for config in menu["customConfigs"]:
            if len(config["mandatoryModifiers"])>=1:
                items_opt.add(menu["name"])
pprint(items_opt)

print("----------------------------------------------------------------------------------------------------")

#7. Count the Number of Salads
#Count and print the total number of unique menu items available in the "Salads & Soups"
#category.
count=0
for catgory in data:
    if catgory["name"]=="Salads & Soups":
        for menu in catgory.get("menuItems") or []:
            print(menu["name"])
            count+=1
print("menu items in salads and soups  :",count)

print("-----------------------------------------------------------------------------------------------------")


#8. Find the Most Expensive Item
#Iterate through all menu items across all categories and find the one with the highest
#itemPrice. Print the item's name and its price.
expensive=0
expensive_item=""
for catagory in data:
    for menu in catagory.get("menuItems") or []:
        for config in menu.get("customConfigs") or []:
            if expensive <= config["itemPrice"]:
                expensive=config["itemPrice"]
                expensive_item=menu["name"]
print(expensive_item," : ",expensive)

''' Find the most expensive item
most_expensive = max(p, key=lambda x: x[1])
print("Most Expensive Item:", most_expensive[0], "Price:", most_expensive[1])'''

print("---------------------------------------------------------------------------------------------------")

#9. Group Items by Price Range
#Create a Python script that categorizes all menu items into three price ranges:
#● Cheap: Under $8.00
#● Moderate: $8.00 - $12.00
#● Expensive: Over $12.00
#Print the names of the items in each category.

priceRange = {
    "cheap": [],
    "moderate": [],
    "expensive": []
}

for category in data:
    for menu in category.get("menuItems") or []:
        for config in menu.get("customConfigs") or []:
            itemPrice = config["itemPrice"]
            price = itemPrice / 90.18

            if price < 8.00:
                if menu["name"] not in priceRange["cheap"]:
                    priceRange["cheap"].append(menu["name"])

            elif 8.00 <= price < 12.00:
                if menu["name"] not in priceRange["moderate"]:
                    priceRange["moderate"].append(menu["name"])

            else:
                if menu["name"] not in priceRange["expensive"]:
                    priceRange["expensive"].append(menu["name"])


pprint(priceRange)

print("-----------------------------------------------------------------------------------------")

#10. Create a Simple Menu Dictionary
#Write a script to transform the JSON data into a simpler dictionary where the keys are the
#main category names (e.g., "Appetizers," "Beverages") and the values are a list of the menu
#item names in that category. Print the resulting dictionary
menu={}

for catagory1 in data:
    catagory=catagory1["name"]
    if catagory not in menu:
        menu[catagory]=[]
    for m in catagory1.get("menuItems") or []:
        menu[catagory].append(m["name"])
pprint(menu)





