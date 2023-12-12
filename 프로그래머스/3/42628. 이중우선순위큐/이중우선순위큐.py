import heapq

def solution(operations):
    queue = []
    for i in operations:
        a, b = i.split()
        if a == 'I':
            heapq.heappush(queue, int(b))
        elif a == 'D' and b == '-1' and queue:
            heapq.heappop(queue)
        elif a == 'D' and b == '1' and queue:
            max_heap = [-x for x in queue]
            heapq.heapify(max_heap)
            max_value = -heapq.heappop(max_heap)
            queue = [-y for y in max_heap]
            heapq.heapify(queue)
            
        if len(queue) == 0:
            answer = [0,0]
        else:
            answer = [max(queue),min(queue)]
    return answer