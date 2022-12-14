def minNumber(arr):
	n=len(arr)
	min=arr[0]
	for i in range(1,n):
		if min>arr[i]:
			min=arr[i]
	return min

print("The minimum number in [465,46,3,9,22,8] is :",
      minNumber([465,46,3,9,22,8]))
def maxNumber(arr):
	n=len(arr)
	max=arr[0]
	for i in range(1,n):
		if max<arr[i]:
			max=arr[i]
	return max

print("The maximum number in [465,46,3,9,22,8] is :",
      maxNumber([465,46,3,9,22,8]))