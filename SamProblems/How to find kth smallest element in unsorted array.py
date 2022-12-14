def sortAlgo(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def smallEle(arr,k):
    arr_sort=sortAlgo(arr)
    print(arr_sort)
    return arr[k-1]
print(smallEle([1,56,35,8,3],3))