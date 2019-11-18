# Insertion Sort

def insert_sort(l):
    for i, n in enumerate(l):
        j = i - 1
        while n < l[j] and j >= 0:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = n
    return l

l = [6,3,4,1,8,5]
result = insert_sort(l)
print(result)       # [1, 3, 4, 5, 6, 8]


# Merge Sort
def _merge(left, right):
    result_list = []
    while left and right:
        result_list.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    if left:
        result_list.extend(left)
    if right:
        result_list.extend(right)
    return result_list

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return _merge(left, right)

l1 = [11,3,6,4,15,5,19,7,17,10,13,8,18,9,2,1,12,16,14,20]
print(merge_sort(l1))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# Quick Sort
def separate(nums, li, ri):
    s = nums[(li + ri) // 2]
    i = li - 1
    j = ri + 1
    while True:
        i += 1
        while nums[i] < s:
            i += 1
        j -= 1
        while nums[j] > s:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(l):
    def _quick(nums, li, ri):
        if li < ri:
            si = separate(nums, li, ri)
            _quick(nums, li, si)
            _quick(nums, si+1, ri)
    _quick(l, 0, len(l)-1)


l2 = [11,3,6,4,15,5,19,7,17,10,13,8,18,9,2,1,12,16,14,20]
quick_sort(l2)
print(l2)       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


