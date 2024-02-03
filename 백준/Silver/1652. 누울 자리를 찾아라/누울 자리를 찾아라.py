import sys

def check_rows(matrix):
    row_counts = 0
    for j in matrix:
        row_length = 0
        for k in list(j.split('X')):
            if len(k) >= 2:
                row_counts += 1
    return row_counts

def check_columns(matrix):
    column_counts = 0
    for l in range(len(matrix)):
        target_column = ''
        for m in matrix:
            target_column += m[l]
        for o in list(target_column.split('X')):
            if len(o) >= 2:
                column_counts += 1
    return column_counts

N = int(sys.stdin.readline())

room = []
for i in range(N):
    row = sys.stdin.readline().strip()
    room.append(row)

print(check_rows(room), check_columns(room))
