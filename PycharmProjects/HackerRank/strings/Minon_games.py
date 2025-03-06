import string

conlist = list(string.ascii_uppercase)
conlist.remove('A')
conlist.remove('E')
conlist.remove('I')
conlist.remove('O')
conlist.remove('U')


def minion_game(strin):
    pointer = 0
    # your code goes here
    l = len(s)
    if 0< l < 10**6:
        done_words_vov = []
        done_words_con = []


        for i in s:
            for p in s:
                if p.isalpha() and 'A' <= p <= 'Z':
                    pass
                else:
                    quit()
            if i in ["A","E","I","O","U"]:
                j=0
                temp_str1 = s[pointer::]
                len_of_temp_str1= len(temp_str1)
                for j in range (len_of_temp_str1):
                    list_attruibute_vov = temp_str1[0:(len(temp_str1)-j)]
                    # (f"{s[(pointer):(len_of_temp_str-j)]}")
                    done_words_vov.append(list_attruibute_vov)
                    # print(done_words_vov)
                pointer += 1

            elif i in conlist :
                l = 0
                temp_str2 = s[pointer::]
                len_of_temp_str2 = len(temp_str2)
                # print(temp_str)
                for i in range(len_of_temp_str2):
                    list_attruibute_con = temp_str2[0:(len(temp_str2)-l)]
                    done_words_con.append(list_attruibute_con)
                    # print(done_words_con)
                pointer += 1

        if len(done_words_vov) > len(done_words_con):
            print(f"Kevin {len(done_words_vov)}")
        elif len(done_words_vov) < len(done_words_con):
            print(f"Stuart {len(done_words_con)}")
        elif len(done_words_vov) == len(done_words_con):
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
# and i not in ["A","E","I","O","U"]



# S = "BANANA"
# print(S[0:3])