for a in range(0,3):
    if True:
        b = 23

for c in range(6,7):
    print(b)
    if True:
        print(b)


nested_list = []
N = int(input())
if 2 <= N <= 5:
    for i in range(N):
        name = input()
        score = float(input())
        raw_list= []
        raw_list.append(name)
        raw_list.append(score)
       # print(raw_list)
        nested_list.append(raw_list)
        raw_list=[]
    # print(nested_list)

# nested_list = [['neha', 23244.0], ['kama', 2332.0], ["kuku", -1],['roni', 2332.0]]
list_of_second_lowest_students = []
lowest_marks = nested_list[0][1]
second_lowest_marks = nested_list[0][1]

for counter in range(len(nested_list)):
    if nested_list[counter][1] < lowest_marks:
        second_lowest_marks = lowest_marks
        lowest_marks = nested_list[counter][1]
        continue
    if (nested_list[counter][1] > lowest_marks) and (nested_list[counter][1] < second_lowest_marks):
        second_lowest_marks = nested_list[counter][1]
        list_of_second_lowest_students = []
        list_of_second_lowest_students.append(nested_list[counter][0])
        continue
    if nested_list[counter][1] == second_lowest_marks:
        list_of_second_lowest_students.append(nested_list[counter][0])
list_of_second_lowest_students.sort()
for i in list_of_second_lowest_students:
    if len(list_of_second_lowest_students) == N:
        break
    else:
        print(i , end='\n')






