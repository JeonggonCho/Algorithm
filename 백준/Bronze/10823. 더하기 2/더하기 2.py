answer = ''

while True:
    try:
        answer += input()
    except:
        break
print(sum(map(int, answer.split(','))))