# n = int(input())
# a = 0
# while a < n:
#     a += 1
#     print(a, end= "")

# n = int(input())
# a = list(map(int, input().strip().split()))[:n]
# a.sort()
# max = max(a)
#
# a.remove(max)
# print(a[-2])

# strings

#
# def count_substring(string, sub_string):
#     counting = 0
#     while sub_string in string:
#         a = string.find(sub_string)
#         string = string[a + 1:]
#         counting += 1
#     return counting
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

n = int(input())
a = 1
while a < n:
    if a == 1:
        number = 1
    elif a == 2:
        number = 22
    elif a == 3:
        number = 333
    elif a == 4:
        number = 4444
    elif a == 5:
        number = 5555
    print(number)
    a += 1