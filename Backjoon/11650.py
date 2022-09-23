N = int(input())
sorted_list = []
for i in range(N):
    f_value, b_value = map(int,input().split())
    sorted_list.append([f_value,b_value])    
sorted_list.sort()
for i in range(N):
    print(sorted_list[i][0],sorted_list[i][1])