"""
快速排序
快速排序(Quick Sort)是一种效率很高的排序算法，是对冒泡排序的一种改进排序算法。
1. 从待排序列表中选取一个基准数据(通常选取第一个数据)。
2. 将待排序列表中所有比基准数据小的元素都放到基准数据左边，所有比基准数据大的元素都放到基准数据右边(升序排列，降序反之)。用基准数据进行分割操作后，基准数据的位置就是它最终排序完成的位置，第一轮排序完成。
3. 递归地对左右两个部分的数据进行快速排序。即在每个子列表中，选取基准，分割数据。直到被分割的数据只有一个或零个时，列表排序完成。
快速排序的时间复杂度为 O(n^2) 。
快速排序是一种不稳定的排序算法
"""

def quick_sort(array, start, end):
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        while array[right] >= mid_data and left < right:
            right -= 1
        array[left] = array[right]
        while array[left] < mid_data and left < right:
            left += 1
        array[right] = array[left]
        array[left] = mid_data
        quick_sort(array, start, left-1)
        quick_sort(array, left+1, end)
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
quick_sort(array, 0, len(array)-1)
print(array)
