class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for words in strs:
            key = tuple(sorted(words))
            if key not in groups:
                groups[key] = [words]

            else:
                groups[key].append(words)

        return list(groups.values())


