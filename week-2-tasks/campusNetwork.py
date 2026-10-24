# DAY 4 CHALLENGE

# Adjacency List Representation of the Campus Network
campusNetwork = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F'],
    'F': ['E']
}

def bfsTraversal(graph, startNode):
    # BFS uses a queue (First-In-First-Out)
    visitedNodes = []
    nodeQueue = [startNode]
    
    while nodeQueue:
        currentNode = nodeQueue.pop(0)
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)
            for neighbor in graph[currentNode]:
                if neighbor not in visitedNodes and neighbor not in nodeQueue:
                    nodeQueue.append(neighbor)
                    
    return visitedNodes

def dfsTraversal(graph, startNode, visitedNodes=None):
    # DFS uses the call stack via recursion (Last-In-First-Out)
    if visitedNodes is None:
        visitedNodes = []
        
    if startNode not in visitedNodes:
        visitedNodes.append(startNode)
        for neighbor in graph[startNode]:
            dfsTraversal(graph, neighbor, visitedNodes)
            
    return visitedNodes

if __name__ == "__main__":
    print("BFS Visit Order:", bfsTraversal(campusNetwork, 'A'))
    print("DFS Visit Order:", dfsTraversal(campusNetwork, 'A'))