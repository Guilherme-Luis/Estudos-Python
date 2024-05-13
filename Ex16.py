from math import ceil
X = float(input("Enter with meter(m²): "))
Y = (X/3)

if (Y <= 18):
    print(f"You have to buy one can of paint")
    print(f"So, you have to spend R$80.00")
else:
    Z = (Y / 18)
    print(f"You have to buy {ceil(Z)} can of pain")
    print(f"So, you have to spend {(80 * (ceil(Z)))}")

