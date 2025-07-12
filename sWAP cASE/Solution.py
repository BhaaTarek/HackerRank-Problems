def swap_case(s):
    chars=list(s)
    for i in chars:
        if i>='A' and i<='Z':
            i=i+32
        elif i>='a' and i<='z':
            i=i-32
    s=''.join(chars)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
