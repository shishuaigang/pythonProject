# 二分查询
# 针对的是有序,有序,有序数组(并且是升序,升序,升序)
def binarySearch(List, target):
    head, tail = 0, len(List) - 1
    while head <= tail:
        mid = head + (tail - head) // 2  # 防止溢出的取中值法
        if List[mid] == target:
            return mid
        if List[mid] < target:
            head = mid + 1
        else:
            tail = mid - 1
    return -1


def binarySearch1(grid, target):
    # 二维数组搜索,二分的思想
    # 从左下角开始，或者右上角开始
    px, py = 0, len(grid[0]) - 1

    while px < len(grid) and py > 0:
        print(grid[px][py])
        if grid[px][py] == target:
            return True
        elif grid[px][py] > target:
            py -= 1
        else:
            px += 1
    return False


if __name__ == "__main__":
    r = binarySearch([1, 3], 2)
    print(r)
    grid = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    r1 = binarySearch1(grid, 6)
    print(r1)
