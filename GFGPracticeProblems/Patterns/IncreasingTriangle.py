"""
*
**
***
****
*****
"""
def increaseTri(n):
    for r in range(n+1):
            print('*  '*r,end='  ')
            print()


if __name__ == '__main__':
    increaseTri(5)