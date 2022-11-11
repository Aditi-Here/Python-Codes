"""Displaying the Keys in sorted order"""
# def dictionairy():
# 	key_value = {}
# 	key_value[2] = 56
# 	key_value[1] = 2
# 	key_value[5] = 12
# 	key_value[4] = 24
# 	key_value[6] = 18
# 	key_value[3] = 323
# 	print("key_value", key_value)
#
# 	# iterkeys() returns an iterator over the
# 	# dictionary’s keys.
# 	for i in sorted(key_value.keys()):
#     	print(sorted(key_value.keys()), end=" ")
#
#
# def main():
# 	dictionairy()
#
# if __name__ == "__main__":
# 	main()

""" Sort the dictionary by key """
# from  collections import OrderedDict
# def dict_sorting():
#     d={}
#     d['a']=1
#     d['b']=2
#     d['e']=3
#     d['d']=4
#     print('dictionary: ',d)
#     sort_d=sorted(d.items())
#     print('sorted dict',sort_d)
#     order_dict=OrderedDict(sort_d)
#     print(order_dict)
#
# def main():
#     dict_sorting()
# if __name__== '__main__':
#     main()

""" Sorting the Keys and Values in Alphabetical Order using the Key """
# d={'a':1,'c':3,'b':2}
# for key in sorted(d):
#     print((key,d[key]),end=" ")

""" Sorting the Keys and Values in alphabetical using the value """
# d={'a':1,'c':3,'v':2}
# def fun():
#     return lambda kv:(kv[1], kv[0])
# for key in sorted(d.items(),key=fun()):
#     print(key)

""" Handling missing keys"""
# d={'a':1,'c':3,'v':2}
# print(d.get('h','Not Found'))

""" Ways to sort list of dictionaries by values in Python – Using itemgetter """
# # Python code demonstrate the working of sorted()
# # and itemgetter
#
# # importing "operator" for implementing itemgetter
# from operator import itemgetter
#
# # Initializing list of dictionaries
# list = [{"name": "Nandini", "age": 20},
# 	{"name": "Manjeet", "age": 20},
# 	{"name": "Nikhil", "age": 19}]
#
# # using sorted and itemgetter to print list sorted by age
# print "The list printed sorting by age: "
# print sorted(list, key=itemgetter('age'))
#
# print("\r")
#
# # using sorted and itemgetter to print
# # list sorted by both age and name
# # notice that "Manjeet" now comes before "Nandini"
# print "The list printed sorting by age and name: "
# print sorted(list, key=itemgetter('age', 'name'))
#
# print("\r")
#
# # using sorted and itemgetter to print list
# # sorted by age in descending order
# print "The list printed sorting by age in descending order: "
# print sorted(list, key=itemgetter('age'), reverse=True)

