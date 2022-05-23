F_i = int(input())
F_I = set(list(map(int,input().split())))
F_s = int(input())
F_S = list(map(int,input().split()))
for i in F_S:
    if i in F_I:
        """ 여기서 set으로 변환하는 작업을 하면 F_S의 길이만큼 set에 대한 
        O(1) * len(F_I) 만큼 늘어난다. 
    """
        print(1)
    else:
        print(0)