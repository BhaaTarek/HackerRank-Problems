n=int(input())
num=map(int, input().split())
b=int(input())
num2=map(int, input().split())

num=set(num)
num2=set(num2)
union=num.union(num2)
print(len(union))
