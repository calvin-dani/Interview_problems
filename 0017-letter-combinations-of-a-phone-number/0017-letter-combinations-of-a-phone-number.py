class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numDig = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"],
        }
        
        def recBuild(idx,temp):
            
            if idx == len(digits):
                res.append(temp)
                return 
            
            for letter in numDig[digits[idx]]:
                recBuild(idx+1,temp + letter)
                
        if digits == "":
            return res
        else:
            recBuild(0,'')
            return res
            