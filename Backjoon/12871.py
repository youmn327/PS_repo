# def GCD(x,y):
#     while(y):
#         x,y = y, x%y
#     return x   

S = input()
T = input()

S_length = len(S)
T_length = len(T)
# string_GCD = GCD(S_length,T_length)

if S * T_length ==  T * S_length:
    print(1)
else:
    print(0)


# if i % 1 == 0:
#         if windows[0] == 0:
#             windows[0] += 1
#         else:
#             windows[0] -= 1
#         if windows[1] == 0:
#             windows[1] += 1
#         else:
#             windows[1] -= 1
        
#         if windows[2] == 0:
#             windows[2] += 1
#         else:
#             windows[2] -= 1
#     elif i% 2 == 0:
#         if windows[1] == 0:
#             windows[1] += 1
#         else:
#             windows[1] -= 1
#     elif i% 2 == 0:
#         if windows[1] == 0:
#             windows[1] += 1
#         else:
#             windows[1] -= 1