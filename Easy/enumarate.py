# Using enumerate to Find Index Positions
a_list = [3,1,3]
def find_indices(list_to_check, item_to_find):
    indices = []
    # print(a_list[1:2])
    for idx, value in enumerate(a_list):
        print("idx value is",idx)
        if value == item_to_find:
            indices.append(idx)
    return indices

print(find_indices(a_list, 3))