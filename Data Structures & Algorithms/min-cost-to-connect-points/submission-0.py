
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x]+=self.size[root_y]
        return True 



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 2d array 
        # points -> [xi, yi], each points[i]
        # cost of connecting two points is manhattan distance
        # return the minimum cost to connect all points together 
        # such that theres exactly one path 
        
        n = len(points)
        edges =[]

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i +1, n):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1-y2)
                edges.append((dist, i, j))

        edges.sort()

        uf = UnionFind(n)
        total_cost = 0 
        edges_used = 0 

        for dist, u , v in edges:
            if uf.union(u,v):
                total_cost += dist
                edges_used += 1 
                if edges_used == n - 1:
                    break

        return total_cost


            