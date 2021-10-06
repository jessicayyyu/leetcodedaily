from collections import deque


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # build graph and indgree mapping
    graph = [[] for i in range(numCourses)]
    indegree = [0] * numCourses

    for in_node, out_node in prerequisites:
        graph[out_node].append(in_node)
        indegree[in_node] += 1

    # check if there is a cycle
    num_node = 0
    q = deque()
    # start from nodes with 0 indegree
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        cur = q.popleft()
        result.append(cur)
        num_node += 1
        for neighbor in graph[cur]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    if num_node == numCourses:
        return result
    else:
        return []
