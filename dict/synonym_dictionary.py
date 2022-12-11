n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[v] = k
    d[k] = v
print(d.get(input()))
