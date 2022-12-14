# arr=[15,25,3,334,345,56]
arr=[-5,-6,-4,-56,59,39,33,99]
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
sort_arr=bubbleSort(arr)
print(sort_arr)
print(sort_arr[len(arr)-1],sort_arr[len(arr)-2])
