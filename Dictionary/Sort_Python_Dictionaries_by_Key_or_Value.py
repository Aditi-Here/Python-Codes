
# Sort by key
"""
Input:
{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output:
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
"""

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

sort_list=list(myDict.keys())
sort_list.sort()
sort_dict={i:myDict[i] for i in sort_list}
print(sort_dict)
