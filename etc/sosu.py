def solution():
    cnt = 0
    for i in range(2,10):
        for j in range(2,i):
            if i % j == 0 :
                cnt+=1
                break
        if cnt == 1:
            cnt = 0 
            continue
        print(i)
print(solution())
