from collections import deque


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def depth_first_search(graph, source):
    stack = deque()
    stack.append(source)
    while len(stack) != 0:
        current_node = stack.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            stack.append(neighbor)


print("DFS")
depth_first_search(graph, "a")


def breadth_first_search(graph, source):
    queue = deque()
    queue.append(source)
    while len(queue) != 0:
        current_node = queue.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            queue.appendleft(neighbor)


print("BFS")
breadth_first_search(graph, "a")
