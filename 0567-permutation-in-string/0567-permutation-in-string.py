class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        freq1 = {}
        freq2 = {}

        for ch in s1:
            if ch not in freq1:
                freq1[ch] = 1
                freq2[ch] = 0
            else:
                freq1[ch] += 1

        idx = 0
        idx2= 0
        while idx <= len(s2) - len(s1):
            if s2[idx] in freq1:
                match = True
                for _ in range(len(s1)):
                    ch = s2[_ + idx]
                    if ch in freq1 and freq1[ch] != freq2[ch]:
                        freq2[ch] += 1
                    else:
                        for reset in range(_):
                            freq2[s2[idx+reset]] = 0
                        match = False
                        break
                if match:
                    return True
                
            idx += 1
                    
        return False
        