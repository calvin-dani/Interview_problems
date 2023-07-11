class Solution:
    def myAtoi(self, s: str) -> int:
        numBuilder = '0'
        isLoading = True
        isSigns = False
        isNeg = False
        s = s.strip()
        for ch in s:
            if (ch == '+' or ch == '-'):
                if isSigns:
                    break
                isNeg = ch == '-'
                isSigns = True
                continue
            elif isLoading and ch.isdigit():
                numBuilder += ch
                isSigns = True
            else:
                isLoading = False

        num,isTrunc = ((2 ** 31),True) if int(numBuilder) / 2 ** 31 >= 1 else (int(numBuilder),False)
        return (num + (0 if isNeg or not isTrunc else -1)) * (-1 if isNeg else 1)

        

            