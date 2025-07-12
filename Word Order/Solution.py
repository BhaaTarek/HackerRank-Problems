n=int(input())
seen=set()
words=[]
counter=[]

for _ in range(n):
    word = input()
    if word in seen:
        i=words.index(word)
        counter[i]+=1
    else:
        seen.add(word)
        words.append(word)
        counter.append(1)

print(len(words))
for c in counter:
    print(c, end=' ')
