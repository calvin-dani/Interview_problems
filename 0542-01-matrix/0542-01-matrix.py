class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        queue = deque()
        visit = []
        
        
        
        def traverse(rIdx,cIdx,step):
            traversalStep = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for x,y in traversalStep:
                xTrav = x + rIdx
                yTrav = y + cIdx
                
                if xTrav < 0 or xTrav >= len(mat) or yTrav < 0 or yTrav >= len(mat[0]) or visit[xTrav][yTrav] == 1:
                    continue
                
                if mat[xTrav][yTrav] == 1:
                    queue.append((xTrav,yTrav,step+1))
                    mat[xTrav][yTrav] = step+1
                visit[xTrav][yTrav] = 1
                
            return
            
        for idxR,row in enumerate(mat):
            visit.append([])
            for idxC, val in enumerate(row):
                if val == 0:
                    visit[idxR].append(1)
                    queue.append((idxR,idxC,0))
                else:
                    visit[idxR].append(0)
                    
        while len(queue) > 0:
            rIdx,cIdx,step = queue.popleft()
            traverse(rIdx,cIdx,step)
            
            
        return mat
            
            
        