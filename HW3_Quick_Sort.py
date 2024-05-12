def QuickSort(array, start, end):
    if start >= end:
        return
    
    pivot = array[start]  # 選擇陣列的第一個元素作為pivot
    left = start + 1
    right = end
    
    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
        print(array)
    
    # 將pivot放到正確的位置
    array[start], array[right] = array[right], array[start]
    
    QuickSort(array, start, right - 1)
    QuickSort(array, right + 1, end)

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
QuickSort(arr, 0, len(arr) - 1)
print(arr)