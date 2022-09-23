n, d = map(int,input().split())
sum_c = 0
for i in range(1,n+1):
    i = str(i)
    count =  i.count(str(d))
    sum_c += count
print(sum_c)