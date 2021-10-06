# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build graph and indegree mapping
    graph = [[] for i in range(numCourses)]
    indegree = [0] * numCourses

    for inNode, outNode in prerequisites:
        graph[outNode].append(inNode)
        indegree[inNode] += 1

    from collections import deque
    q = deque()
    # find all nodes with 0 indegree
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    # check if there is a cycle
    numNode = 0
    while q:
        node = q.popleft()
        numNode += 1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return numNode == numCourses
