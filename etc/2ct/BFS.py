from collections import deque
from turtle import Turtle

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.pop()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.appendleft(i)
                visited[i] = True

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

bfs(graph, 1, visited)
