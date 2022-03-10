#https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0 :
                cnt+=1
        if cnt % 2 == 0:
            answer+=i
        else :
            answer -= i
    return answer
"""
테스트 1 〉	통과 (24.43ms, 10.1MB)
테스트 2 〉	통과 (4.07ms, 10.2MB)
테스트 3 〉	통과 (4.04ms, 10.1MB)
테스트 4 〉	통과 (3.34ms, 10.1MB)
테스트 5 〉	통과 (19.76ms, 10.1MB)
테스트 6 〉	통과 (1.08ms, 10.1MB)
테스트 7 〉	통과 (0.43ms, 10.1MB)
"""

def solution(left, right):
    answer = 0
    lst = [i for i in range(left,right+1)]
    for i in set(lst):
        cnt = 0
        for j in range(1,i+1):
            if i%j == 0 :
                cnt+=1
        if cnt % 2 == 0:
            answer+=i
        else :
            answer -= i
    return answer


"""
정확성  테스트
테스트 1 〉	통과 (20.21ms, 10.2MB)
테스트 2 〉	통과 (3.57ms, 10.2MB)
테스트 3 〉	통과 (4.15ms, 10.3MB)
테스트 4 〉	통과 (1.75ms, 10.2MB)
테스트 5 〉	통과 (20.46ms, 10.2MB)
테스트 6 〉	통과 (1.04ms, 10.2MB)
테스트 7 〉	통과 (0.42ms, 10.3MB)

"""


"""
약수의 개수가 홀수인 경우는 제곱수로 나누어 지는 경우가 있을 수 있다.

"""