def fact(n):
    if n == 0:
        return 1
    else:
        return n*(fact(n-1))


fact_num = [fact(i) for i  in range(21)]

num = int(input())

if num == 0 :
    print("NO")
else:
    for i in range(20,-1,-1):
        if num >= fact_num[i]:
            num -= fact_num[i]
    print("YES") if num == 0 else print("NO")
        