def solution(citations):
    citations.sort(reverse=True)
    for index , citation in enumerate(citations):
        if index >= citation:
            return index
    return len(citations)