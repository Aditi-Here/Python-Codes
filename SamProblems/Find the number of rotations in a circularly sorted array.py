# Function to find the total number of times the list is rotated

# def findRotationCount(nums):
#     # search space is nums[left…right]
#     (left, right) = (0, len(nums) - 1)
#
#     # loop till the search space is exhausted
#     while left <= right:
#
#         # if the search space is already sorted, we have
#         # found the minimum element (at index `left`)
#         if nums[left] <= nums[right]:
#             return left
#
#         mid = (left + right) // 2
#
#         # find the next and previous element of the `mid` element (in circular manner)
#         next = (mid + 1) % len(nums)
#         prev = (mid - 1 + len(nums)) % len(nums)
#
#         # if the `mid` element is less than both its next and previous
#         # neighbor, it is the list's minimum element
#
#         if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
#             return mid
#
#         # if nums[mid…right] is sorted, and `mid` is not the minimum element,
#         # then the pivot element cannot be present in nums[mid…right],
#         # discard nums[mid…right] and search in the left half
#
#         elif nums[mid] <= nums[right]:
#             right = mid - 1
#
#         # if nums[left…mid] is sorted, then the pivot element cannot be present in it;
#         # discard nums[left…mid] and search in the right half
#
#         elif nums[mid] >= nums[left]:
#             left = mid + 1
#
#     # invalid input
#     return -1
#

def findRotationCount(num):
    low=0
    high=len(num)-1
    while high>=low:
        mid=low+(high-low)//2
        if num[low]<num[high]:
            return low
        next=(mid+1)%len(num)
        prev=(mid-1+len(num))%len(num)

        if num[mid]<=num[next] and num[mid]<=num[prev]:
            return mid
        if num[mid]<=num[high]:
            high=mid-1
        if num[mid]>=num[low]:
            low=mid+1
    return -1

if __name__ == '__main__':
    # nums = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    nums=[8,9,10,2,5,6]
    print(f'The list is rotated {findRotationCount(nums)} times')
