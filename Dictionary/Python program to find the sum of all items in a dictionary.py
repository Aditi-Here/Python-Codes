# Python program to find the sum of all items in a dictionary
"""
Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600

"""
input = {'a':100,'b':200,'c':300}
output=0
for key,val in input.items():
    output+=val
print(output)