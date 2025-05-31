def twosum(list1, target):
    hashmap = {}
    for i, n in enumerate(list1):
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i
    return

print(twosum([2,7,11,15], 9))