# https://www.acmicpc.net/problem/1057 ja
"""
1번 부터 N번까지 배정
인접한 번호 끼리 스타 대결
홀수면 마지막 번호 부전승
서로 대결하기 전까지는 계속 우승
몇 라운드에서 대결이 펼쳐지는가?
만약 대결하지 않을때는 -1 출력
"""



N, K, O = map(int,input().split())
cnt = 0
user_len = 0
user = [i for i in range(1,N+1)]
if len(user) // 2 < len(user) / 2 :
    user_len = (len(user) // 2 )+1
else :
    user_len = len(user) // 2

for i in range(1,user_len) :
    pass 
