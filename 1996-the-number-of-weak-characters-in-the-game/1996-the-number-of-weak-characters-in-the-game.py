class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        if len(properties) == 0:
            return 0
        properties.sort(reverse = True ,key= lambda a : (a[0],-a[1]))
        
        maxDef = properties[0][1]
        maxAtk = properties[0][0]
        count = 0
        print(properties)
        for prop in properties:
            if prop[1] < maxDef and prop[0] != maxAtk:
                count += 1
            if prop[1] >= maxDef:
                maxDef = prop[1]
                maxAtk = prop[0]

        return count