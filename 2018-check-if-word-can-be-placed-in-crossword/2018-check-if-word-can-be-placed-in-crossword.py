import re
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
       
        def getPatternForArray(arrayPattern):
            pattern = []
            for ele in arrayPattern:
                if ele == ' ':
                    pattern.append('.')
                else:
                    pattern.append(ele)
            
            patternStr = ''.join(pattern)
            return patternStr.split('#')

        patternDic = set()

        for row in board:
            for pattern in getPatternForArray(row):
                patternDic.add(pattern)

        for col in range(len(board[0])):
            tempArr = []
            for row in range(len(board)):
                tempArr.append(board[row][col])
            for pattern in getPatternForArray(tempArr):
                patternDic.add(pattern)
        
        print(patternDic)
        wordRev = word[::-1]
        for pattern in patternDic:
            if re.search('.',pattern) and len(pattern) == len(word):
                patternRegFw = re.search('{}'.format(pattern),word)
                patternRegBk = re.search('{}'.format(pattern),wordRev)
                if patternRegFw or patternRegBk:
                    return True
        
        return False

        