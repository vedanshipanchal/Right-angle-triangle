n = int(input("Enter rows:"))

for i in range(n):
    for stars in range (i+1):
        print("*",end="")
    print("\n")