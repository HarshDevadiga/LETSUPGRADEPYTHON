
for c in range(1041999,702648266):

    order=len(str(c))
    sum=0
    t=c
    while t >0:
        d=t%10
        sum=sum+d**order
        t //= 10

        if c==sum:
             print(c)
