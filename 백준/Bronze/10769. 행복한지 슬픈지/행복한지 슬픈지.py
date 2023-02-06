import sys

chars = sys.stdin.readline()
emoticon =  ''
happy_num = 0
sad_num = 0

for i in chars:
    if i in [':', '-', '(', ')']:
        emoticon += i
    if emoticon == ':-)':
        happy_num += 1
        emoticon = ''
    elif emoticon == ':-(':
        sad_num += 1
        emoticon = ''
        
if happy_num != 0 or sad_num != 0:
    if happy_num > sad_num:
        print('happy')
    elif happy_num < sad_num:
        print('sad')
    else:
        print('unsure')
elif happy_num == 0 and sad_num == 0:
    print('none')