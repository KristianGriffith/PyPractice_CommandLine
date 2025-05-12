#lbs to kg or kg to lbs

typ = input("Enter the type of weight to be entered")
amt = float(input("Enter the amount: "))

if typ == "kg":
    adj_weight = amt * 2.20462
    print(f"The weight in lbs is {round(adj_weight, 2)}")
elif typ == "lbs":
    adj_weight = amt / 2.20462
    print(f"The weight in kg is {round(adj_weight, 2)}")
