# First occurance
def firstOccurance(arr,key):
    low=0
    high=len(arr)-1
    ans=-1
    while high>=low:
        mid=low+(high-low)//2
        if arr[mid]==key:
            high=mid-1
            ans=mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return ans

# Last occurance
def lastOccurance(arr,key):
    low=0
    high=len(arr)-1
    ans=-1
    while high>=low:
        mid=low+(high-low)//2
        if arr[mid]==key:
            low=mid+1
            ans=mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return ans

if __name__=='__main__':
    arr=[1,2,3,3,3,3,3,5,5]
    x=firstOccurance(arr,5)
    y=lastOccurance(arr,5)
    print(x,y)