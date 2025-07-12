if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])

    worstGrade = 100000
    for i in list1:
        if i[1] < worstGrade:
            secondWorstGrade = worstGrade
            worstGrade = i[1]
        if i[1] < secondWorstGrade and i[1] > worstGrade:
            secondWorstGrade = i[1]

    list2 = []
    for i in list1:
        if i[1] == secondWorstGrade:
            list2.append(i[0])

    list2 = sorted(list2)
    for i in list2:
        print(i)
