class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        romNum = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }
        subtraction = {
            1000 : 100,
            500 : 100,
            100 : 10,
            50 : 10,
            10: 1,
            5 : 1,
            1 : 0

        }
        nums = [ 1000,500,100,50,10,5,1]

        while num > 0:
            for redNum in nums:
                temp = num // redNum
                if temp >= 1:
                    res += romNum[redNum] * (temp)
                    num -= redNum * (temp)

                if num + subtraction[redNum] >= redNum:
                    res += romNum[subtraction[redNum]] + romNum[redNum]
                    num -= ( redNum - subtraction[redNum])
                
                # print(num)
        return res