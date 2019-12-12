count=int(0)
sum=int(0)
for j in range(200,1000000):
        n=int(j)
        i=int(j)

        sum=0
        while(i>0):
           sum+=int((i%10)**5)
           i=int(i/10)

        if(sum==n):
            count+=sum


print(count)


