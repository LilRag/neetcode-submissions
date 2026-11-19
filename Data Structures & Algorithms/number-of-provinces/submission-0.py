class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n cities , some are connected, some are not 
        # if city a is connected directly with city b , and city b is connected with city c 
        # then city a is also connected to city c indirectly

        # province is a group of directly or indirectly connected cities 

        n = len(isConnected)
        parent = [i for i in range(n)]
        size = [1]*n
        provinces = n 

        def find(x:int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]


        def union(x:int , y:int)->None:
            nonlocal provinces

            boss_x = find(x)
            boss_y = find(y)

            if boss_x == boss_y:
                return 

            if size[boss_x] < size[boss_y]:
                boss_x , boss_y = boss_y , boss_x

            parent[boss_y] = boss_x
            size[boss_x] += size[boss_y]
            provinces -= 1 


        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i,j)

        return provinces
