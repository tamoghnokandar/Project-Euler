def lcm(x,y):
    a=x
    b=y
    while(a!=b):
            if(a>b):
                a=a-b
                if(b>a):
                    b=b-a
    return ((y*x)/a)




ans=1
i = 1
for i in range(1, 3):
    ans = lcm(ans, i)
print(ans)