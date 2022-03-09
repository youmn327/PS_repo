#https://www.acmicpc.net/problem/1252

"""
하나씩 탐색이 아닌 전체적으로 보는 생각을 하자
숫자의 범위가      
"""


N1, N2 = map(str,input().split())
result = []
temp = 0


# if len(N1) > len(N2):
#     for i in range(-1,-(len(N2))-1,-1):
#         print(int(N1[i]),int(N2[i]),temp)
#         re_n = int(N1[i])+int(N2[i])+temp
#         print(re_n)
#         if re_n == 2:
#             re_n = 0
#             temp = 1
        
#         if re_n == 3:
#             re_n = 1
#             temp = 1
        
#         result.append(re_n)
#     N1 = reversed(N1[:-(len(N2))])
#     result = ''.join(map(str, result))
#     result += ''.join(map(str, N1)) 
#     result.split()
#     result = reversed(result)
#     result = ''.join(map(str, result))


# print(result)
        
