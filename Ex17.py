from math import ceil, floor
X = float(input("Enter with meter(m²): "))
Y = (X/3)

if (Y <= 18):
    Z = (Y / 3.6)
    print(f"""
        You have to buy one of this:
        So, you have to spend R$80.00 in one can of paint
        Or, you have to spend R${(25 * (ceil(Z)))} on {ceil(Z)} gallon
    """)
else:
    Z = (Y / 18)
    G = (Y / 3.6)
    M = (3.6 / (Z - (floor(Z))))
    print(f"""
        You have to buy one of this:
        So, you have to spend R${(80 * (ceil(Z)))} in {ceil(Z)},
        Or, you have to spend R${(25 * (ceil(G)))} on {ceil(G)} gallons,
        Or, you have to spend R${(80 * (floor(Z))) + (M * 25)} in {floor(Z)} can of paint and {M} gallons
    """)