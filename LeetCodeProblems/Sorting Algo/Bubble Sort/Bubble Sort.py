#  Program to implement bubble sort
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__=="__main__":
    array=[2,2,3,3,1,5,4]
    bubbleSort(array)
    print(array)
