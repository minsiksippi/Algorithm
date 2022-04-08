def DFS(n, computers, com, visit):
    visit[com]=True
    
    for connect in range(n):
        if com!=connect and computers[com][connect]==1 and visit[connect]==False:
            DFS(n, computers, connect, visit)


def solution(n, computers):
    answer = 0
    visit = [False for i in range(n)]
    
    for com in range(n):
        if visit[com]==False:
            DFS(n, computers, com, visit)
            answer+=1
            
    return answer
