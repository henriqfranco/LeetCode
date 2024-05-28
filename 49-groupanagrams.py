from collections import defaultdict

def groupAnagrams(strs):
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            hashmap[tuple(count)].append(s)
            
        return hashmap.values()
    
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))