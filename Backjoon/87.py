n = int(input())
count = 0 

coin_check = [500,100,50,10]
for coin in coin_check:
    count += n//coin
    n %= coin
print(count)