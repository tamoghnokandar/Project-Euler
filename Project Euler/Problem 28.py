sum=int(0)
carry=int(2)
term=int(1)
count=int(1001)
while(count>0):
    sum+=term
    term+=carry
    carry+=2
    count-=1




Sum=int(0)
Carry=int(4)
Term=int(1)
Count=int(1001)
n=int(2)
while(Count>0):
            Sum+=Term
            Term+=Carry
            n-=1
            Count-=1
            while(n==0):
                    Carry+=4
                    n=2


print(Sum+sum-1)