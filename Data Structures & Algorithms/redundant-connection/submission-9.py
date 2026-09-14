class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)] #[0,1,2,3...]
        rank = [1] * (len(edges) + 1) #[1,1,1...] component size

        def find(n): #get the root
            p = parent[n]
            while p != parent[p]: #find root, when p == parent[p] that is root
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2): #join the roots, or return False
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False #cycle found
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1 #join them
                rank[p1] += rank[p2] #add sizes
            else:
                parent[p1] = p2 #join
                rank[p2] += rank[p1] #add sizes
            return True #that means merge successful

        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2] #return the redundant edge 
                
