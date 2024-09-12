def mutate_string(string, position, character):
    string = s
    position = int(i)
    character = c
    lis = list(string)
    lis[int(i)] = c
    return ''.join(lis)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)