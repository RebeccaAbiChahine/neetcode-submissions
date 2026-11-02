class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid = undirected acyclic graph
        # -> we want to verify that there's no cycles

        edgeMap = {}

        for i in range(n):
            edgeMap[i] = []

        visit = set()

        for node, edge in edges:
            edgeMap[node].append(edge)
            edgeMap[edge].append(node) # undirected so both ways
        
        def dfs(node, parent):

            if node in visit:
                return False
            
            visit.add(node)
            
            for edge in edgeMap[node]:
                if edge == parent:
                    continue

                if not dfs(edge, node):
                    return False

            return True


        if not dfs(0, -1):
            return False

        return len(visit) == n



        