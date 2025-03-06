nested_list = []
N = int(input())
if 2 <= N <= 5:
    for i in range(N):
        name = input()
        score = float(input())
        raw_list= []
        raw_list.append(score)
        raw_list.append(name)

        # print(raw_list)
        nested_list.append(raw_list)
        raw_list=[]
    # print(nested_list)


# nested_list = [[-50, 'neha'], [-50,'junn'], [-50 , "wdq"],[51 , 'asd']]
# print(nested_list[])

list_of_second_lowest_students = []
lowest_marks = nested_list[0][1]            #-50
second_lowest_marks = nested_list[0][1]     #-50

# nested_list = [[37.21, 'Harry'], [37.21,'berry'], [37.2, "tina"],[41, 'akriti'],[39,'harsh']]
nested_list.sort()
# N = len(nested_list)
# print(nested_list[1][0])
second_Score_index = None
second_score = None
second_score_name_list = []
for i in range(1,len(nested_list)):
    if nested_list[i][0] != nested_list[0][0]:
        second_score = nested_list[i][0]
        # print(second_score)
        second_Score_index = i
        break
for i in range(0,len(nested_list)):
    if nested_list[i][0] == second_score:
        second_score_name_list.append(nested_list[i][1])

second_score_name_list.sort()
# print(second_score_name_list)
for i in second_score_name_list:
    if len(second_score_name_list) == N:
        break
    else:

        print(i, end='\n')















