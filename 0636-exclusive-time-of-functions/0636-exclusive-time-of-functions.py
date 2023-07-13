class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        callStack = []
        funcTime = [0] * n 
        time = 0
        for idx,exec in enumerate(logs): 
            func = exec.split(':')
                 
            if func[1] == 'start':
                if len(callStack) > 0:
                    funcTime[callStack[-1]] += int(func[2]) - time
                time = int(func[2])
                callStack.append(int(func[0]))
                
            else:
                funcTime[callStack[-1]] += int(func[2]) - time + 1 
                time = int(func[2]) + 1
                callStack.pop()
            
            
        return (funcTime)