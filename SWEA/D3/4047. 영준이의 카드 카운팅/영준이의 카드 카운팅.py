T = int(input())

for i in range(1, T+1):
    cards = input()
    cards_li = []
    length = len(cards) // 3
    cards_cnt = {'S':13, 'D':13, 'H':13, 'C':13}

    for j in range(length):
        card = cards[j * 3:j * 3 + 3]
        cards_li.append(card)

    if len(cards_li) != len(set(cards_li)):
        print(f'#{i} ERROR')
    else:
        for k in cards_li:
            cards_cnt[k[0]] -= 1
        print(f'#{i}', *cards_cnt.values())