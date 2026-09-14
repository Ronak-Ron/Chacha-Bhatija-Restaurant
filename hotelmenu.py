#Define the menu of restuatrant
menu = {
    'Poori Sabzi': 70,
    'Rajma Rice' : 90,
    'Kadi Rice'  : 90,
    'Chole Rice' : 90,
    'Kachori Sabzi' : 60,
    'Raita'         : 20,
    'Samosa'        : 20,
    'Bread Pakora'  : 30,
    'Chole Bathure' : 120,
    'Gulab Jamun'   : 40,
}
# Greetings
print("Welcome to Chacha-Bhatija Restautrant")
print("Please find our menu presented below :-")

for key, value in menu.items():
    print(key,":","Rs",value)

order_total = 0

order_1 = input("Enter the name of the dish you would like to have = ")
if order_1 in menu:
    order_total += menu[order_1]
    print(f"Your item {order_1} has been added to your order")
else:
    print(f"This is not in the list{order_1}", "Enter something else!")

# If customer would like to add something.

while True:
    order = input("Do you want to add more ? (or type 'No' to finish): ")
    if order.lower() == "no":
        break
    elif order in menu:
        order_total += menu[order]
        print(f"{order} added to your order.")
    else:
        print(f"{order} is not in the menu. Please try again.")


print(f"Your total bill is Rs {order_total}. Thank you for visiting Chacha-Bhatija Restaurant!")
