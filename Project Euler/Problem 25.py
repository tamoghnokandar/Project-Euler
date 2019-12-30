def fibonacci(n):
    fib=[1,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]
i=1
while(True):
        if(len(str(fibonacci(i)))==1000):
            print(i)
            break
        i+=1