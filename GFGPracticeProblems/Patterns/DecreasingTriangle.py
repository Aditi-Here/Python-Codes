"""
* * * * *
* * * *
* * *
* *
*
"""
def decTrian(n):
    for r in range(5):
        print('*  '*(n-r),end='')
        print()

if __name__ == '__main__':
    decTrian(5)