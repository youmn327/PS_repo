def solution(n, words):
    answer = []
    empty_value = len(words)
    check_word = words[0]
    check_lastword = words[0][-1]
    cnt = 0
    start_n = 0
    for i in words[1:]:
        
        
        
        print(check_word,check_lastword,cnt,start_n)
        if start_n == n+1:
            cnt += 1
            start_n = 0
        
        if check_lastword != i[0] or check_word != i:
            empty_value -=1
            return [start_n,cnt]
            

        check_word = i
        check_lastword = i[-1]
        
        cnt += 1
        start_n +=1
        
    if empty_value == len(words):
            return [0,0]    

    return answer