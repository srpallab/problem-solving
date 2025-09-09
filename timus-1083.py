n, k = input().split()

n = int(n)
k_len = len(k)
sum = n


for i in range(1, n):
    if i * k_len < n:
        sum *= (n - (i * k_len))
print(sum)
