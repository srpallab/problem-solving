n = int(input())
if n == 0:
    print(1)
elif n > 0:
    print(n*(n+1)//2)
else:
    print((n*(n-1)//2)* -1 +1)