"""冒泡排序"""
def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
"""插入排序"""
def InsertionSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
"""快速排序"""
def QuickSort(arr, left, right):
    # 递归退出的条件
    if left >= right:
        return
    # 设定起始的基准元素
    key = arr[left]
    # l为序列左边在开始位置的由左向右移动的游标
    l = left
    # r为序列右边末尾位置的由右向左移动的游标
    r = right
    while l < r:
        # 如果l与r未重合，r(右边)指向的元素大于等于基准元素，则r向左移动
        while arr[r] >= key and l < r:
            r -= 1
        # 走到此位置时r指向一个比基准元素小的元素,将r指向的元素放到l的位置上,此时r指向的位置空着,接下来移动l找到符合条件的元素放在此处
        arr[l] = arr[r]
        # 如果l与r未重合，l(右边)指向的元素小于等于基准元素，则l向右移动
        while arr[l] <= key and l < r:
            l += 1
        # 此时l指向一个比基准元素大的元素,将l指向的元素放到r空着的位置上,此时l指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
        arr[r] = arr[l]
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    # 将基准元素放到该位置,
    arr[l] = key
    # 对基准元素左边的子序列进行快速排序
    QuickSort(arr, left, l-1)
    # 对基准元素右边的子序列进行快速排序
    QuickSort(arr, l+1, right)
"""希尔排序"""
def ShellSort(arr):
    length = len(arr)
    # 1. 设置步长
    step = length // 2
    while step > 0:
        for i in range(step,length):
            temp = arr[i]
            j = i
            while j >= step and arr[j-step] > temp:
                arr[j] = arr[j-step]
                j -= step
            print(i)
            print(temp)
            arr[j] = arr[i]
        step //= 2
"""选择排序"""
def SelectionSort(arr):
    length = len(arr)
    for i in range(length-1):
        temp = arr[i]
        minIndex = i
        for j in range(i+1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
"""堆排序"""
# 二叉树很容易就存储在数组中。位置 k 的节点的父节点位置为 k/2，而它的两个子节点的位置分别为 2k + 1和 2k+2
def heapsort(array):
    # 遍历非叶子节点，建立堆结构数组
    length = len(array)
    for i in range(length-1, -1, -1):
        adjustHeap(array, i, length)
        print("arr of heap:", array)
    # 堆积树建立完成，开始排序
    for j in range(length-1, 0 ,-1):
        array[0], array[j] = array[j], array[0]
        print(array)
        adjustHeap(array, 0, j)
# 维护堆的性质
def adjustHeap(array, i, length):
    # 对第i号进行堆调整，获取非叶子节点数据
    temp = array[i]
    # 非叶子节点的左子节点
    k = 2 * i + 1
    # 遍历对比k后面的节点，把temp放入合理的位置
    while k < length:
        # k+1 < length 确保有左右节点才比较
        if k + 1 < length and array[k] < array[k+1]:
            # 如果左子节点比右子节点小，k就切换到右子节点
            k += 1
        # 如果子节点有更大的
        if array[k] > temp:
            # 父节点替换为更大的
            array[i] = array[k]
            # 记录当前最大点位置
            i = k
        else:
            # 因为堆的特点，后面的更不满足
            break
        # k 切换到下一个左子节点
        k = 2 * k + 1
    # 此时i是空位，i上层的都比temp大，temp放到这里
    array[i] = temp
"""归并排序"""
def mergeSort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    return merge(mergeSort(left),mergeSort(right))
# 合并两个有序的数组
def merge(left, right):
    array = []
    length_left = len(left)
    length_rigth = len(right)
    l = r = 0
    while  length_left > l and length_rigth > r:
        if left[l] <= right[r]:
            array.append(left[l])
            l += 1
        else:
            array.append(right[r])
            r += 1
    # 谁还有剩余就把谁全部放进去
    if l == length_left:
        for i in right[r:]:
            array.append(i)
    else:
        for i in left[l:]:
            array.append(i)
    return array
"""计数排序"""
def counting_sort(array):
    # 找出数列中最大值和最小值 创建min-max这么多个0用来统计数列中每个值出现的次数，再从最小值依次排放到最大值
    # 找到最大值
    max_num = max(array)
    # 找到最小值
    min_num = min(array)
    # 负数数列
    neg_list = []
    # 非负数数列
    pos_list = []
    # 对负数和非负数分别处理
    for num in array:
        if num < 0:
            neg_list.append(num)
        elif num >= 0:
            pos_list.append(num)
    length_neg_list = len(neg_list)
    length_pos_list = len(pos_list)
    # 对负数数列进行处理
    if length_neg_list != 0:
        # 创建从最最小值到0来累计每个负数出现的次数
        neg_count_list = [0 for _ in range(min_num, 0)]
        length_neg_count_list = len(neg_count_list)
        # 对于负数列中的每个值+1操作
        for i in range(length_neg_list):
            neg_count_list[neg_list[i]] += 1
        #初始化排序索引为0
        neg_index = 0
        # 对于计数列表中的每一项
        for i in range(-length_neg_count_list,0):
            # 不为0表明有计数
            while neg_count_list[i] > 0:
                # 依次排放数值
                neg_list[neg_index] = i
                # 每次排放后索引加1
                neg_index += 1
                # 每次排放后对应的计数减1
                neg_count_list[i] -= 1
    if length_pos_list != 0:
        # 创建从0到最大值到来累计每个正数出现的次数
        pos_count_list = [0 for _ in range(0, max_num+1)]
        length_pos_count_list = len(pos_count_list)
        # 对于负数列中的每个值+1操作
        for i in range(length_pos_list):
            pos_count_list[pos_list[i]] += 1
        # 初始化排序索引为0
        pos_index = 0
        # 对于计数列表中的每一项
        for i in range(length_pos_count_list):
            # 不为0表明有计数
            while pos_count_list[i] > 0:
                # 依次排放数值
                pos_list[pos_index] = i
                # 每次排放后索引加1
                pos_index += 1
                # 每次排放后对应的计数减1
                pos_count_list[i] -= 1
    result_list = neg_list + pos_list
    return result_list
"""桶排序"""
"""
计数排序的改进版
找出数列中最大值和最小值 创建min-max这么多个桶用来统计数列中每个值出现的次数，再从第一个桶倾倒到最后一个桶
"""
def bucket_sort(array):
    length_array = len(array)
    # 找到最大值
    max_num = max(array)
    # 找到最小值
    min_num = min(array)
    bucket_list = [0 for _ in range(max_num-min_num+1)]
    length_bucket_list = len(bucket_list)
    # 添加值到对应的桶内，对应桶计数+1
    for i in range(length_array):
        bucket_list[array[i] - min_num] += 1
    # 结果列表
    print(bucket_list)
    result_list = []
    for i in range(length_bucket_list):
        print(i)
        if bucket_list[i] != 0:
            result_list += [i+min_num] * bucket_list[i]
    return result_list
"""基数排序"""
"""
比较位数上的值
比较每一位上的数字大小，当每一位比较完成排序也就完成
"""
def radix_sort(array):
    # 找到最大值
    max_num = max(array)
    # 找到最小值
    min_num = min(array)
    # 负数数列
    neg_list = []
    # 非负数数列
    pos_list = []
    # 对负数和非负数分别处理
    for num in array:
        if num < 0:
            neg_list.append(num)
        elif num >= 0:
            pos_list.append(num)
    length_neg_list = len(neg_list)
    length_pos_list = len(pos_list)
    # 负数进行排序
    if length_neg_list != 0:
        neg_num_digit = 0
        while neg_num_digit < len(str(min_num)):
            # 初始化数值列表
            neg_values_lists = [[] for _ in range(10)]
            # 对于数列中的每个数
            for neg_num in neg_list:
                neg_values_lists[int(neg_num/(10**neg_num_digit)) % 10].append(neg_num)
            print(neg_values_lists)
            neg_list.clear()
            for neg_value_list in neg_values_lists:
                for neg_num in neg_value_list:
                    neg_list.append(neg_num)
            # 比较下一位
            neg_num_digit += 1
    # 正数进行排序
    if length_pos_list != 0:
        pos_num_digit = 0
        while pos_num_digit < len(str(max_num)):
            # 初始化数值列表
            pos_values_lists = [[] for _ in range(10)]
            # 对于数列中的每个数
            for pos_num in pos_list:
                pos_values_lists[int(pos_num / (10 ** pos_num_digit)) % 10].append(pos_num)
            pos_list.clear()
            for pos_value_list in pos_values_lists:
                for pos_num in pos_value_list:
                    pos_list.append(pos_num)
            # 比较下一位
            pos_num_digit += 1
    result_list = neg_list + pos_list
    return  result_list

arr = [6, 9, 3, 4, 8, 5, 2, 1, 7,-1,-5]
print(arr)
res = radix_sort(arr)
print(res)