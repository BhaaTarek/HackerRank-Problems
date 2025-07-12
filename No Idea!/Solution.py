n, m = map(int, input().split())
arr = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

A = set(A)
B = set(B)

happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        continue

print(happiness)
