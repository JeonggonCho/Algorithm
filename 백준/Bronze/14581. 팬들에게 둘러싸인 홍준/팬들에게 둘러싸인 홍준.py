import sys

fan = ':fan:'

char = sys.stdin.readline().strip()

id = ':' + char + ':'

print(fan * 3, fan + id + fan, fan * 3, sep='\n')