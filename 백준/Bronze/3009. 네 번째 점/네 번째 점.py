x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
if x[0] == x[1]:
    x_num = x[2]
elif x[0] == x[2]:
    x_num = x[1]
elif x[1] == x[2]:
    x_num = x[0]
if y[0] == y[1]:
    y_num = y[2]
elif y[0] == y[2]:
    y_num = y[1]
elif y[1] == y[2]:
    y_num = y[0]
print(x_num, y_num)