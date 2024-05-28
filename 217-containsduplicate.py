def containsdup(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(containsdup([1, 2, 3, 1]))