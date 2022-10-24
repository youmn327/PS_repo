N = int(input())
card_lst = [i for i in range(1,N+1)]
cnt = 1
emt_card = []
while len(emt_card) <= N-1:
    if cnt%2 == 0:
        card_lst.append(card_lst[0])
        card_lst.pop(0)
    else :
        emt_card.append(card_lst[0])
        card_lst.pop(0)
    cnt +=1
for i in emt_card:
    print(i,end=" ")