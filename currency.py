print("___________________________________________")
print("Enter the currency you are converting FROM:")
print("1: USD to UGX")
print("2: UGX to USD")
print("3: USD to IRN")

currency_From = input("Seletect a number that represents the kind of operation you need to perfom : ")
print("___________________________________________")


amount = float(input("Enter amount: "))

print("___________________________________________")

# print("Enter the currency you are converting TO:")
# currency_To = input("USD,UGX,EUR,NGN,SDG,CDF: ")
# print("___________________________________________")

if currency_From == "1":
    ugxAmount = amount * 3700.0
    print(f"The UGX amount : {ugxAmount} UGX")
elif currency_From == "2":
    usdAmount = amount / 3700.0
    print(f"The USD amount : {usdAmount} USD")
    
else:
    print("[INFO]: Invalid Choice")
