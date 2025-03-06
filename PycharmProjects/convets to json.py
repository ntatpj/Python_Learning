json_list_of_dictionaries=[]
file = open("file.txt",'r')
n=0
for line in file:
    # current_line_list=line.splitlines()
    # print(current_line_list)
    # print(f"line no {n}: {line}")
    # n +=1
    current_line=line.split()
    # print(len(current_line))
    dict={}
    dict["cmd"]=current_line[8]
    dict["permission"]=current_line[0]
    dict["user"]=current_line[2]
    dict["group"]=current_line[3]
    dict["file_size"]=current_line[4]
    dict["date_of_last_edit"]=current_line[5]
    json_list_of_dictionaries.append(dict)
print(json_list_of_dictionaries)