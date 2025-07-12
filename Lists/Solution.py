if __name__ == '__main__':
    N = int(input())
    list = []
    i = 0
    while i < N:
        command = input()
        commandParts = command.split()

        if commandParts[0] == 'insert':
            list.insert(int(commandParts[1]), int(commandParts[2]))
        elif commandParts[0] == 'print':
            print(list)
        elif commandParts[0] == 'remove':
            list.remove(int(commandParts[1]))
        elif commandParts[0] == 'append':
            list.append(int(commandParts[1]))
        elif commandParts[0] == 'sort':
            list.sort()
        elif commandParts[0] == 'pop':
            list.pop()
        elif commandParts[0] == 'reverse':
            list.reverse()

        i = i + 1
