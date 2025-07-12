if __name__ == '__main__':
    s = input()
    counter = [0, 0, 0, 0, 0]
    for i in s:
        if i.isalnum():
            counter[0] += 1

        if i.isalpha():
            counter[1] += 1

        if i.isdigit():
            counter[2] += 1

        if i.islower():
            counter[3] += 1

        if i.isupper():
            counter[4] += 1

    for i in counter:
        if i > 0:
            print("True")
        else:
            print("False")
