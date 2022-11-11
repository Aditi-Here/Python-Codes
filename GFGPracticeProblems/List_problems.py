"""Python program to interchange first and last elements in a list"""
 # my approach
# li = [1,2,3,4,5,6]
# first = li[0]
# last=li[-1]
# li[0]=last
# li[-1]=first
# print(li)
#
# # another approach
# li=[1,2,3,4,5,6]
# li[0],li[-1]=li[-1],li[0]
# print(li)

""" Python program to swap two elements in a list """
# # Given a list in Python and provided the positions of the elements,
# # write a program to swap the two elements in the list.
# # my approach
# li=[1,2,3,4,5,6]
# def list_swap(list,pos1,pos2):
#     list[pos1],list[pos2]=list[pos2],list[pos1]
#     return list
# swap_list=list_swap(li,1,3)
# print('swap list',swap_list)

""" Python | Ways to find length of list """
# li = [1,2,3,4,5,6]
# # Method 1: Naive Method
# counter=0
# for i in li:
#     counter+=1
# print(counter)

""" Maximum of two numbers in Python """
# # Method 1:
# a,b=4,6
# def maxNumber(a,b):
#     if a>b :
#         print(" {} is greater than {}".format(a,b))
#     else:
#         print('{} is greater than {}'.format(b,a))
#
# maxNumber(a,b)
#
# #  Method 2:
# c = max(a,b)
# print(c)
#
# # Method 3:
# c = [a if a>b else b]

""" Count occurrences of an element in a list """
# #  Method 1
# li = [1,1,1,1,1,1,1,1,1,1,3,4,5,6,7,8,9]
# print(li.count(1))
#
# # Method 2
# count=0
# for i in li:
#     if i==1:
#         count+=1
# print(count)

""" Find sum and average of List in Python """
# # Method 1
# li = [1,2,3,4,5,6]
# print(sum(li))
# print(sum(li)/len(li))
# #   Method 2
# sum=0
# for i in li:
#     sum=sum+i
# print(sum,sum/len(li))

""" Sum of number digits in List """
# #  Method 1
# li=[12,23,45,75,78,22,33]
# sum_list=[]
# for i in li:
#     digit_count=0
#     for digits in str(i):
#         digit_count+=int(digits)
#     sum_list.append(digit_count)
# print(sum_list)
#  Method 2
# li=[12,45,63,49,12,666]
# sum_of_digits=[[digit_count+=1 for digits in str(i)] for i in li]

""" Python program to print all odd numbers in a range """
# # Method 1:
# def odd_numbers(start,end):
#     odd_list=[]
#     for i in range(start,end):
#         if i%2!=0:
#             odd_list.append(i)
#     print(odd_list)
# odd_numbers(4,12)

# # Python program to print Even Numbers in given range
#
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
#
# #create a list that contains only Even numbers in given range
# even_list = range(start, end + 1)[start%2::2]
#
# for num in even_list:
# 	print(num, end = " ")

# li = [1,2,3,4,5]
# even_numbers=[i for i in li if i%2== 0]
# print(even_numbers)


""" Find char count in string """

# li="Aditi"
# count_dict={}
# for i in li:
#     if i in count_dict.keys():
#         count_dict[i]=count_dict[i]+1
#     else:
#         count_dict[i] = 1
#
# print(count_dict)

""" Python program to find smallest number in a list """

# input_list=[11,5,3]
# # using ascending sorting
# input_list.sort()
# print('smallest number= ',input_list[0])
# # using descending sorting
# input_list.sort(reverse=True)
# print('smallest number is : ',input_list[len(input_list)-1])
# # using min function
# small_item=min(input_list)
# print('smallest number= ',small_item)
# # by comparing all numbers
# min=input_list[0]
# for i in input_list[1:]:
#     if i<min:
#         min=i
# print(min)
