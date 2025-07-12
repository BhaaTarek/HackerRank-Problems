M=int(input())
a= list(map(int,input().split()))
N= int(input())
b= list(map(int,input().split()))

a=set(a)
b=set(b)

union=a.union(b)
intersection=a.intersection(b)

answer=union-intersection

answer=sorted(answer)

for i in answer:
    print(i)
