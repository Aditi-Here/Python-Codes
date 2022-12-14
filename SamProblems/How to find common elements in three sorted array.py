# arr1=[1,2,3,4]
# arr2=[3,4,5,6]
# arr3=[3,4,5,8]
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1=len(arr1)
common=[]
for i in arr1:
    if (i in arr2) and (i in arr3):
        common.append(i)
print(common)

