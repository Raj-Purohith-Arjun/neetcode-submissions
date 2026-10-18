class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ck in s:
                count[ord(ck) - ord('a')] += 1

            anagmap[tuple(count)].append(s)
        return list(anagmap.values())    
