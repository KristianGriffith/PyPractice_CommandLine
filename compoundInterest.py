#Python Compound interest calculator

initialPrincipal = float(input("Enter the initially deposited amount: "))
duration = int(input("Enter the duration of time the money will be left in the back: "))
rate = int(input("Enter Rate per year, as a %: "))
principal = initialPrincipal


for i in range(0,duration):
    amt = float(rate/100 * principal)
    principal = principal + amt

print(principal)







