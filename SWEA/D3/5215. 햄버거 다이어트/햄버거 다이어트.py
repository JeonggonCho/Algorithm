from itertools import combinations

results = []

T = int(input())  # 테스트케이스 수 T

for i in range(1, T + 1):
    N, L = map(int, input().split())  # 재료 수 N, 제한 칼로리 L
    max_score = 0

    ingredients = []
    for j in range(N):
        S, K = map(int, input().split())  # 점수 S, 칼로리 K
        ingredients.append((S, K))

    for l in range(1, N + 1):
        combi_ingredients = list(combinations(ingredients, l))  # 재료 조합 생성
        for m in combi_ingredients:
            total_calorie = sum(ingredient[1] for ingredient in m)
            if total_calorie <= L:
                total_score = sum(ingredient[0] for ingredient in m)
                max_score = max(max_score, total_score)

    results.append(f'#{i} {max_score}')

for o in results:
    print(o)
