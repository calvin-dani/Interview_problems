class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def calDistance(p1,p2):
            
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
        
        freq = {}
        
        points = [p1,p2,p3,p4]
        points.sort()
        ptr1 = 0
        ptr2 = 1
        
        while ptr1 < len(points):
            ptr2 = ptr1 + 1
            while ptr2 < len(points):
                dist = calDistance(points[ptr1],points[ptr2]) 
                if dist == 0:
                    return False
                elif dist in freq:
                    freq[dist] += 1
                else:
                    freq[dist] = 1
                ptr2 += 1
            ptr1 += 1
        
        if len(freq) == 2:
            val = set(freq.values())
            
            return True if 4 in val and 2 in val else False
        
        return False
                