class Queue: 
    def __init__(self):
        self.queue = []

    def enqueue(self,v):
        self.queue.append(v)

    def isempty(self):
        return (self.queue == [])

    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]

        return v 

    def __str__(self):
        return(str(self.queue))

    
def BFSList(AList, start_vertex, visited):
    q = Queue()
    visited[start_vertex] = True 
    q.enqueue(start_vertex)

    while (not q.isempty()):
        curr_vertex = q.dequeue()
        for adj_vertex in AList[curr_vertex]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True 
                q.enqueue(adj_vertex)

    return visited


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Alist = {i: [] for i in range(n)}

        for a,b in edges:
            Alist[a].append(b)
            Alist[b].append(a)

        visited = {}

        for each_vertex in Alist.keys():
            visited[each_vertex] = False
        count = 0 

        for vertex in range(n):
            if not visited[vertex]:
                BFSList(Alist, vertex, visited)
                count += 1 

        return count