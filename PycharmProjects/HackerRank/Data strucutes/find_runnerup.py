# number_of_students = int(input("Enter the total number of students participated"))
# details = input("Enter the score of all students with space")
# details_in_array = details.split()
# print(details_in_array)
# # print(dir(details_in_array))
# details_in_array.sort()
# print(details_in_array)
# print(f"Runnerup is {details_in_array[number_of_students-2]}")



# number_of_students = int(input("Enter the total number of students participated"))
# if (2 <= number_of_students <= 10):
#     details = input("Enter the score of all students with space")
#     details_in_array = details.split()
#     # print(dir(details_in_array))
#     details_in_array.sort()
#     print(details_in_array)
#     if (-100 <= int(details_in_array[0]) and int(details_in_array[number_of_students-1]) <= 100):
#         # print(details_in_array)
#         for i in range(number_of_students):
#             if details_in_array[number_of_students-1] != details_in_array[number_of_students-(i+1)]:
#                 print(f"Runnerup is {details_in_array[number_of_students-(i+1)]}")
#                 break
#             # else:
#             #     continue
#     else:
#         print("SCore should be between -100 to 100")
# else:
#     print("the number of students must be between 2 to 10")
#



number_of_students = int(input())
if (2 <= number_of_students <= 10):
    details = input()
    details_in_array = details.split()
    details_in_array = [int(x) for x in details_in_array]
    # print(dir(details_in_array))
    details_in_array.sort()
    print(details_in_array)
    if (-100 <= int(details_in_array[0]) and int(details_in_array[number_of_students-1]) <= 100):
        print(details_in_array)
        for i in range(number_of_students):
            if details_in_array[number_of_students-1] != details_in_array[number_of_students-(i+1)]:
                print(details_in_array[number_of_students-(i+1)])
                break

