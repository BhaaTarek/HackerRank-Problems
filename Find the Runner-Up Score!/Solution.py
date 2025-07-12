if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maximum=-100
    previous_maximum=-100
    for i in arr:
        if i>maximum:
            previous_maximum=maximum
            maximum=i
        elif i>previous_maximum and i<maximum:
            previous_maximum=i
    runnerUpScore=previous_maximum
    print(runnerUpScore)
