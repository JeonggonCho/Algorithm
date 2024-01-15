class Node:
    def __init__(self, data_node, left_node, right_node):
        self.data_node = data_node
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, dict, result):
    if node.left_node is not None:
        in_order(tree[node.left_node], dict, result)
    result.append(dict[node.data_node])
    if node.right_node is not None:
        in_order(tree[node.right_node], dict, result)


for i in range(1, 11):
    N = int(input())
    dict = {}
    tree = {}
    result = []
    for j in range(N):
        input_data = input().split()
        data_node = input_data[0]
        data = input_data[1]
        dict[data_node] = data
        if len(input_data) == 2:
            left_node = None
            right_node = None
        elif len(input_data) == 3:
            left_node = input_data[2]
            right_node = None
        else:
            left_node = input_data[2]
            right_node = input_data[3]
        tree[data_node] = Node(data_node, left_node, right_node)

    in_order(tree['1'], dict, result)
    answer = ''.join(result)
    print(f'#{i} {answer}')