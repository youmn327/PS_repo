#https://leetcode.com/problems/word-ladder/
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    def onestep(word1, word2): # 한 글자만 다르니?
        return sum([c1 != c2 for (c1, c2) in zip(word1, word2)]) == 1


    start, end, M = beginWord, endWord , 1000000 # M은 엄청 큰 숫자
    V = {"hit":1, "hot":M, "dot":M, "dog":M, "lot":M, "log":M, "cog":M}  # 방문하지 않은 단어들

    while V:
        v, dist = min(V.items(), key=lambda x: x[1])
        V.pop(v)
        if v == end:
            print(dist)
            break

        for word in V:
            if onestep(v, word) and dist+1 < V[word]:
                V[word] = dist + 1