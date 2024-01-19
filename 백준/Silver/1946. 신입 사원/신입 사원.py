import sys

def max_new_employees(applicants):
    applicants.sort(key=lambda x: x[0])  # 서류심사 성적을 기준으로 정렬
    max_rank = applicants[0][1]  # 첫 지원자의 면접 성적으로 초기화
    count = 1  # 첫 지원자는 무조건 선발

    for k in range(1, len(applicants)):
        doc_rank, interview_rank = applicants[k]
        if interview_rank <= max_rank:
            count += 1
            max_rank = interview_rank

    return count

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    applicants = []

    for j in range(N):
        grades = list(map(int, sys.stdin.readline().split()))
        applicants.append(grades)

    result = max_new_employees(applicants)
    print(result)