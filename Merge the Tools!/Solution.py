def merge_the_tools(string, k):
    t = []
    split = ""
    i = 0
    while i < len(string):
        j = 0
        while j < k:
            split = split + string[i]
            j += 1
            i += 1
        t.append(split)
        split = ""

    split = ""
    u = []
    for s in t:
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
                split += char
        u.append(split)
        split = ""

    for i in u:
        print(i)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
