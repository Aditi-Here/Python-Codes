def PalinArray(arr, n):
	# Code here
	Flag = False

	for i in range(n):
		arr[i]=str(arr[i])
		arr_len = len(arr[i])
		if arr_len==1:
			Flag=True
		mid=arr_len//2
		for j in range(mid):
			if arr[i][j] == arr[i][arr_len - (j + 1)]:
				Flag = True
			else:
				Flag = False
				return 0


	if Flag:
		return 1
	else:
		return 0


# x=PalinArray([1001, 2002 ,3121 ,3003, 5005 ,6006],6)
x=PalinArray([9],1)
print(x)

