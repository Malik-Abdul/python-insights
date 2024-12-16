def BubbleSort(arr):
    arrLength = len(arr)
    for k in range(arrLength):
        swapped = False 
        # for j in range(arrLength-1):
        for j in range(arrLength-k-1):
            if arr[j] > arr[j+1]:
                swapped = True
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if not swapped:
            print("Breaking")
            break
    return arr

    

print(BubbleSort([4,7,1,99,2]))