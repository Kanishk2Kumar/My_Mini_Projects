n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

average_marks = float((student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2])/3)
format_average = "{:.2f}".format(average_marks)
print(format_average)
