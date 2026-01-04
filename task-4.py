from task_4_base import Node, draw_tree


def visualize_heap(heap):
    if not heap:
        return

    nodes = [Node(value) for value in heap]

    for i in range(len(nodes)):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(nodes):
            nodes[i].left = nodes[left]
        if right < len(nodes):
            nodes[i].right = nodes[right]

    draw_tree(nodes[0])


if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3]
    visualize_heap(heap)