class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result =[]
        keys={}
        for i in range(len(strs)):
            sort=''.join(sorted(strs[i]))
            if sort in keys:
                result[keys[sort]].append(strs[i])
            else:
                keys[sort]=len(result)
                result.append([strs[i]])
        return result