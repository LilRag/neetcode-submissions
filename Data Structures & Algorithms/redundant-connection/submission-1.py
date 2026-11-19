class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1]*(n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]


        def union(x,y):

            boss_x = find(x)
            boss_y = find(y)

            if boss_x == boss_y:
                return False

            if size[boss_x] < size[boss_y]:
                boss_x, boss_y = boss_x, boss_y

            parent[boss_y] = boss_x
            size[boss_x] += size[boss_y] 

            return True 

        for u,v in edges:
            if not union(u,v):
                return [u,v]

        return []