X = float(input("Enter with Size of File(MB): "))
Y = float(input("Enter with speed of ethernet(Mbpsd): "))
print(f"Your download will take {((((X*8) / Y) / 60))} minutes")