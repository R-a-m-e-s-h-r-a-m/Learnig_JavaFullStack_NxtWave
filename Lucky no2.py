a = input()

if (int(a) % 9 == 0) or (a[0]=="9" or a[1]=="9"):
    print("Lucky Number")
else:
    print("Unlucky Number")