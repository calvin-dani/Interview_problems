class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recGen(temp,openP,closeP):
            if openP == closeP and openP == 0:
                res.append(''.join(temp))
                return
            if openP == closeP:
                recGen(temp + ['('],openP - 1,closeP)
            elif openP == 0:
                recGen(temp + [')'],openP,closeP - 1)
            else:
                recGen(temp + ['('],openP - 1,closeP)
                recGen(temp + [')'],openP,closeP - 1)
        recGen([],n,n)
        return res