class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = {}
        for x in strs:
            if(not(''.join(sorted(x)) in temp)):
                temp[''.join(sorted(x))] = []
            temp[''.join(sorted(x))].append(x)
            
        return temp.values()
        