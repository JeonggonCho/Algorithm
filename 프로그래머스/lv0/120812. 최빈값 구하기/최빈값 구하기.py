def solution(array):
	count = [0] * (max(array)+1)
    
	for i in array:
		count[i] += 1
	cnt = 0
	for j in count:
		if j == max(count):
			cnt += 1
	if cnt > 1:
		return -1
	else:
		return count.index(max(count))