"""
Given a sorted binary array, efficiently count the total number of 1’s in it.

For example,

Input:  nums[] = [0, 0, 0, 0, 1, 1, 1]

Output: The total number of 1’s present is 3


Input:  nums[] = [0, 0, 1, 1, 1, 1, 1]

Output: The total number of 1’s present is 5
"""
# def countOnes(input):
#     count=0
#     for num in input:
#         if num==1:
#             count+=1
#     return count
#
# # if '__name__'=='__main__':
# input=[0, 0, 0, 0, 1, 1, 1]
# output=countOnes(input)
# print('The total number of 1’s present is ',output)

# def binarySearch(v, To_Find):
# 	lo = 0
# 	hi = len(v) - 1
#
# 	# This below check covers all cases , so need to check
# 	# for mid=lo-(hi-lo)/2
# 	while hi - lo > 1:
# 		mid = (hi + lo) // 2
# 		if v[mid] < To_Find:
# 			lo = mid + 1
# 		else:
# 			hi = mid-1
#
# 	if v[lo] == To_Find:
# 		print("Found At Index", lo)
# 	elif v[hi] == To_Find:
# 		print("Found At Index", hi)
# 	else:
# 		print("Not Found")
#
#
# if __name__ == '__main__':
# 	v = [1, 3, 4, 5, 6]
#
# 	To_Find = 1
# 	binarySearch(v, To_Find)
#
# 	To_Find = 6
# 	binarySearch(v, To_Find)
#
# 	To_Find = 10
# 	binarySearch(v, To_Find)
#
# # This code is contributed by Tapesh(tapeshdua420)

# def findOnesBinarySearch(input,key,low,high):
#     # low=0
#     # high=len(input)-1
#     count=0
#     if low>high:
#         return False
#     else:
#         mid=low+(high-low)//2
#         if input[mid]==1 and input[mid-1]==0:
#             return mid;
#         if input[mid-1]==1:
#             return findOnesBinarySearch(input,1,low,mid-1)
#         else:
#              return findOnesBinarySearch(input,1,mid+1,high)
def firstOccurance(input,key):
    start=0
    end=len(input)-1

    ans=-1
    while start<=end:
        mid = start + (end - start) // 2
        if input[mid]==key:
            ans=mid
            end=mid-1
        elif input[mid]<key:
            start=mid+1
        elif input[mid]>key:
            end=mid-1
    return ans

def lastOccurance(input,key):
    start=0
    end=len(input)-1

    ans=-1
    while start<=end:
        mid = start + (end - start) // 2
        if input[mid]==key:
            ans=mid
            start=mid+1
        elif input[mid]<key:
            start=mid+1
        elif input[mid]>key:
            end=mid-1
    return ans


if __name__ == '__main__':
    input = [0, 1, 1, 1, 1,1,1,1,1,1]
    count=lastOccurance(input,1)-firstOccurance(input,1)+1
    print('count of i is :',count)
    # count=findOnesBinarySearch(input,1,0,len(input))
    # print('count',len(input)-count)



