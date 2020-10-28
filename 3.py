# 各种简单的排序
import random


def selectSort(List):
    # 选择排序，依次将最小的值放置在列表的最左边
    i = 0
    while i < len(List) - 1:
        minVal = List[i]
        for j in range(i + 1, len(List)):
            if List[j] < minVal:
                minVal = List[j]
                List[i], List[j] = List[j], List[i]
        i += 1
    return List


def mergeSort(List):
    # 递归
    if len(List) <= 1:
        return List
    mid = List[len(List) // 2]
    left = mergeSort([item for item in List if item < mid])
    middle = [item for item in List if item == mid]
    right = mergeSort([item for item in List if item > mid])
    return left + middle + right


def bubbleSort(List):
    # 冒泡排序
    for i in range(len(List)):
        for j in range(i + 1, len(List)):
            if List[i] > List[j]:
                List[i], List[j] = List[j], List[i]
    return List


if __name__ == "__main__":
    L = [random.randint(1, 10000000) for _ in range(10000)]
    print(selectSort(L))
    print(mergeSort(L))
    print(bubbleSort(L))
