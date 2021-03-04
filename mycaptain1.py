n = input("Enter total no.: ")

n1=0
n2=1
sum=0
if n==1:
    print(n1)
else:
    while(sum<=n):
        print(n1)
        temp = n1+n2
        n1=n2
        n2=temp
        sum+=1