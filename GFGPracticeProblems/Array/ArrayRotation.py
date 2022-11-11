# def arrarRotation(A,D,N):
#     arr = []
#     arr=A[D:]+A[0:D]
#     return arr

# Rotate one by one
def arrarRotation(A,D,N):
    temp=[]
    while D>0:
        temp=A[0]
        A=A[1:]
        A.append(temp)
        D-=1
    return A

if __name__=='__main__':
    a=arrarRotation([1,2,3,4,5],2,5)
    print(a)