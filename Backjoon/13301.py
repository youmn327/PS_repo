#https://www.acmicpc.net/problem/13301
start_arr = [0,1]
t = int(input())
for i in range(t-1):
    start_arr.append(start_arr[i]+start_arr[i+1])

print((start_arr[-1]+(start_arr[-1]+start_arr[-2]))*2)