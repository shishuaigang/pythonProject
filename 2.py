# 二分查询
# 针对的是有序数组
def erfen(List, target):
    head, tail = 0, len(List) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if List[mid] == target:
            return mid
        if List[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return -1


if __name__ == "__main__":
    r = erfen([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
    print(r)
