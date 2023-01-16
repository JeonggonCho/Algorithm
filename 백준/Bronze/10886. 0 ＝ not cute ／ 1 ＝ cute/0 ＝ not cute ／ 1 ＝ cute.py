N = int(input())
cute = 0
list1 = []

for i in range(N):
    a = int(input())
    cute += a
    list1.append(a)
if cute > (len(list1)/2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")