import time
start=time.time()
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

count=1
x=3
y=2
while(count!=10001):
                    if(isprime(x)):
                            count+=1
                            y=x
                    x+=2
print(y)
end=time.time()
print(end-start)
