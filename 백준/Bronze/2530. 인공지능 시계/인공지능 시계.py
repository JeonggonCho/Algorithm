import sys

h, m, s = map(int, sys.stdin.readline().split())

time = int(sys.stdin.readline())

sec = (s + time) % 60
m_time = (s + time) // 60

minute = (m + m_time) % 60
h_time = (m + m_time) // 60

hour = (h + h_time) % 24

print(hour, minute, sec)