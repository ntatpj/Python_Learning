strs = ["flower","flow","flight"]
smallest_word = ""
smallest_words_ka_lenght  = len(strs[0])
smallest_words_ka_index =0
for i in strs:
    if len(i) < smallest_words_ka_lenght:  #5<6 6<5 4 < 5
        smallest_words_ka_lenght = len(i) #5 4
        smallest_word = strs[smallest_words_ka_index]  # strs[1] flown
    smallest_words_ka_index += 1  # 1/ +2
# print(smallest_words_ka_lenght)
# print(smallest_word)

# LOGIC I
result = []
last_index_of_smallest_word = len(smallest_word)
for j in range(smallest_words_ka_lenght):
    for i in range(len(strs)):
        # print(i)
        matching = 0
        if strs[i].startswith(smallest_word):
            matching =1
        else:
            smallest_word = smallest_word.removesuffix(smallest_word[-1])
            break

print(smallest_word)

# LOGIC II
# print(small.removesuffix(small[-1]))

# for q in range(smallest_words_ka_lenght):
#     for k in range(len(strs)):
#         is_same = False
#         if strs[k][q]==smallest_word[q]:
#             # print(strs[k][q])
#             is_same=True
#         else :
#             break
#     if is_same == True:
#         result.append(smallest_word[q])
#
# print(result)
# print("".join(result))