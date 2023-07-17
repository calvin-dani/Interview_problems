class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        dictionary.sort(key = lambda i: (-len(i), i))
        for word in dictionary:
            
            ptr1 = 0
            
            for ch in s:
                if word[ptr1] == ch:
                    ptr1 += 1
                if ptr1 == len(word):
                    return word
            
            
        return ""