# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
i=0
s=set()
while i<N:
    stamp=input()
    s.add(stamp)
    i=i+1
print(len(s))
