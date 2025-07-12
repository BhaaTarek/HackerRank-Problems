def count_substring(string, sub_string):
    count = 0
    i = 0
    j = 0
    while i < len(string):
        if string[i] == sub_string[0]:
            k = i
            j = 0
            while j < len(sub_string) and k < len(string):
                if string[k] != sub_string[j]:
                    break
                j = j + 1
                k = k + 1
            if j == len(sub_string):
                count = count + 1
        i = i + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
