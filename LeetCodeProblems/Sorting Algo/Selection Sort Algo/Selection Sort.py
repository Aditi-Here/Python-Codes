 # Program to implement selection sort
def selectionSort(arr):
     n=len(arr)
     for i in range(n):
         min_idx=i
         for j in range(i,n):
             if arr[j]<arr[min_idx]:
                 min_idx=j
         arr[i],arr[min_idx]=arr[min_idx],arr[i]

def test1():
    array = [8, 6, 1, 2, 9, 1]
    selectionSort(arr=array)
    print(array)

def test2():
    input=[9,8,7,6,5,1,2]
    result=[1,2,5,6,7,8,9]
    selectionSort(input)
    if input==result:
        return print('Test case Passed')
    else:
        return print('Test case Fail')
if __name__=='__main__':
    test2()