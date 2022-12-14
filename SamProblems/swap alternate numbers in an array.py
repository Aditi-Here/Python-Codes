arr=[1,2,3,4,5,6]
n=len(arr)
for i in range(0,n,2):
    print(i)
    temp=arr[i]
    arr[i]=arr[i+1]
    arr[i+1]=temp
print(arr)