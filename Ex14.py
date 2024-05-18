X = float(input("Enter with fish weight(Kg): "))
if (X > 50):
    Y = (X - 50)
    Z = (Y * 4.0)
    print(f"The penaly will cost: R${Z}")
else:
    print("You don't need to pay the penaly")