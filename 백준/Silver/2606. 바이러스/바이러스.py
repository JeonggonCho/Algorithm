import sys

node_num = int(sys.stdin.readline())
network_num = int(sys.stdin.readline())

graph = [[] for i in range(node_num + 1)]

for j in range(network_num):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

start_num = 1
visited = [False] * (node_num + 1)

stack = [start_num]
visited[start_num] = True

while stack:
    cur = stack.pop()
    for k in graph[cur]:
        if not visited[k]:
            visited[k] = True
            stack.append(k)
            
print(visited.count(True)-1)