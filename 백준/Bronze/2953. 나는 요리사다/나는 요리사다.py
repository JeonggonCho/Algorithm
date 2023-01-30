import sys

score_matrix = [sum((list(map(int, sys.stdin.readline().split())))) for i in range(5)]
print(score_matrix.index(max(score_matrix))+1, max(score_matrix))