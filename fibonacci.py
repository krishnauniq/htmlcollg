n=int(input("Enter a number  "))
n1=int(n/2)
for i in range(2,n1+1):
    if n/i!=0 :
        print("prime")
        break
    else:
        print("not prime")
        break