def union(arr1,arr2):
    n2 = len(arr2)
    union_list = []
    for i in range(n2):
        if arr2[i] not in arr1:
            union_list.append(arr2[i])
    arr1=arr1+union_list
    return arr1
def intersection(arr1,arr2):
    n1=len(arr1)
    inter_list=[]
    for i in range(n1):
        if arr1[i] in arr2:
            inter_list.append(arr1[i])
    return inter_list
arr1=[1,2,3,4,5,6]
arr2=[4,5,6,7,8,9]
inter=intersection(arr1,arr2)
print("intersection :",inter)
union_arr=union(arr1,arr2)
print('union ',union_arr)
