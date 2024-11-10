n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i 

for i in range(1,n+1):
    if i==1:
        s = ""
        for j in range(1,n+1):
            s += str(sum) + " "
            sum -= 1
        print(s)
    elif i==n:
        print("1")
    else:
        print(str(sum)+" " + "  "*(n-i-1) + str(sum - (n-i)))
        sum -= (n-i+1)