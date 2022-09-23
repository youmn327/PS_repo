n = int(input())
string_list = [input() for _ in range(n)]
sorted_lst = []
dictionary = {string : i for i,string in enumerate(string_list)}

for i in dictionary.keys():
    sorted_lst.append(i)

sorted_lst = sorted(sorted_lst)	
sorted_lst = sorted(sorted_lst, key = len)	
for i in sorted_lst:
    print(i)