# Name      :Kristian Griffith
# Date      :Due 12th May 2025
# Definition:


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
concession = {"Popcorn" : float("2.00"),
              "Hot Dog" : float("2.00"),
              "Giant Pretzel Dog": float("2.00"),
              "Asst Candy" : float("1.00"),
              "Soda": float("1.00"),
              "Bottled Water": float("1.00")}


print("\n\t\t-------------MENU-----------")
for key, value in concession.items():
    print(f"\t\t{key:20} : ${value:.2f}")
print("\t\t----------------------------\n")

cart = {}
cost = []
# i = 0
amt = 0


while True:
    item = input("Select an item from the list: ")
    if not concession.get(item):
        continue
    if cart.get(item):
        cart [item] = cart[item] + concession[item]
    else:
        cart.update({item : float(concession[item])})

    goAgain = input("Does that complete your order? ").lower()
    if goAgain == "no":
        continue

    else:
        clear_screen()
        print("\n\t\t-------------CART-----------")
        gross = 0
        for key, value in cart.items():
            print(f"\t\t{key:20} : ${value:.2f}")
            gross += value
        tab =""
        print(f"\n\t\tSubtotal{tab:12} : ${gross:.2f}")
        VAT = 0.175 * gross
        print(f"\t\tVAT(17.5%){tab:10} : ${VAT:.2f} ")
        total = gross + VAT
        print(f"\t\tTotal{tab:15} : ${total:.2f}")
        print("\t\t----------------------------\n")
        break
