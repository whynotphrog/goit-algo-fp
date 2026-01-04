from collections import deque
from task_4_base import Node, draw_tree


def generate_colors(n):
    colors = []
    for i in range(n):
        value = int(255 * i / max(1, n - 1))
        colors.append(f"#{value:02x}{value:02x}ff")
    return colors


def bfs(root):
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    colors = generate_colors(len(order))
    for node, color in zip(order, colors):
        node.color = color

    draw_tree(root)


def dfs(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    colors = generate_colors(len(order))
    for node, color in zip(order, colors):
        node.color = color

    draw_tree(root)


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.right = Node(1)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right.right = Node(3)

    bfs(root)
    dfs(root)