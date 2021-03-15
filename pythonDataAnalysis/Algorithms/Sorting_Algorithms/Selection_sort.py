def selection_sort(arr):
    swap_happened = True
    while swap_happened:
        print("Selection sort status: " + str(arr))
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num+1] > arr[num]:
                swap_happened = True
                arr[num+1], arr[num] = arr[num], arr[num+1]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

selection_sort(l)