arr=[1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
dict={}
for i in arr:
    if i not in dict.keys():
        dict[i]=arr.count(i)

print(dict)
for key,value in dict.items():
    if value==1:
        print(key)
