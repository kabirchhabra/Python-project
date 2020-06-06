
n = int(input("No. of terms: "))

n1 = 0
n2 = 1
i = 0

if(n<0):
    print("Invalid number")

while(i<n):
    print(n1)
    nt = n1+n2

    n1 = n2
    n2 = nt

    i+=1
