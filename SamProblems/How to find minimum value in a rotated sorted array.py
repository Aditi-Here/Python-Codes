def minRotate(arr):
    n=len(arr)
    low=0
    high=n-1
    while high>min:
        mid=low+(high-low)//2
        next=(mid-1)%n