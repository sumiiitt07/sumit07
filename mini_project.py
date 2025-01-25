menu={
    "paneer":40,
    "samosa":20,
    "litti":50,
}
print("Welcome to my restaurant : ")
print("paneer :Rs40\nsamosa :Rs50\nlitti :Rs50\n")


total_order=0

item_1=input("enter the items name u want to order : ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"your item { item_1} in ordered in our list")

else:
    print(f"your ordered item {item_1} is not our list")

another_item = input("Do u want to order another item (yes/no)")
if another_item=="yes":
    item_2=input("Enter the another items u wants to order :")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"item {item_2} has been ordered ")
    else:
        print(f"you ordered item {item_2} is not available")

print("the total amount of ur items is ",total_order)