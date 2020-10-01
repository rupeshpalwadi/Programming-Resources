def bubblesort(arr):
    n = len(arr)

    for i in range(n):

        # Elements before i are already sorted
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

arr = [7, 1, 4, 6, 2, 3, 4, 4, 5]
print(bubblesort(arr))
