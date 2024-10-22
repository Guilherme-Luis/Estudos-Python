X = float(input("Enter with your salary(H): "))
Y = float(input("Enter with your worked hours in the month: "))
Z = (X*Y)

print(f"""Your  total salary is R${(Z)}, but bro, don't forget the taxes for government
    You need to pay R${(Z*0.08):.2f} in INSS.
    You need to pay R${((Z*0.05)):.2f} in Syndicate.
    You need to pay R${(Z*0.11):.2f} in Income tax.
    Your final salary is: R${(Z - ((Z*0.08) + (Z*0.05) + (Z*0.11))):.2f}
""")