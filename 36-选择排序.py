"""
选择排序
选择排序首先从待排序列表中找到最小(大)的元素，存放到元素列表的起始位置(与起始位置进行交换)，作为已排序序列，第一轮排序完成。然后，继续从未排序序列中找到最小(大)的元素，存放到已排序序列的末尾。直到所有元素都存放到了已排序序列中，列表排序完成。

选择排序每次都是去找最小(大)的元素，隐含了一种挑选的过程，所以被称为选择排序。
时间复杂度为 O(n^2) 。一种不稳定的排序算法
"""
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
for i in range(len(array) - 1):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    if min_index != i:
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
print(array)