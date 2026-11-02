class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # count of connected components 
        # for i in range(n)
        #     dfs()
        #    res += 1

        edgeMap = {i : [] for i in range(n)}

        for node, edge in edges:
            edgeMap[node].append(edge)
            edgeMap[edge].append(node)


        visit = set()
        res = 0

        def dfs(node):
            if node in visit:
                return 
                
            visit.add(node)
            for edge in edgeMap[node]:
                dfs(edge)
                

        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res