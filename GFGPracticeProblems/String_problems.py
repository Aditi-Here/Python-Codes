""" Python program to check whether the string is Symmetrical or Palindrome """
# Given a string. the task is to check if the string is symmetrical and palindrome or not.
# A string is said to be symmetrical if both the halves of the string are the same and
# a string is said to be a palindrome string if one half of the string is the reverse of the other half
# or if a string appears same when read forward or backward.
# input_str = "khobkho"
# def symmetry_check(input_str):
#     centre=len(input_str)//2
#     print(type(centre))
#     if centre%2==0:
#         first_part = input_str[0:centre]
#         second_part=input_str[centre:]
#     else:
#         first_part = input_str[0:centre]
#         second_part = input_str[centre+1:]
#     if first_part==second_part:
#         print('Symmetrical string')
#     else:
#         print("Not Symmetric string")
#
# symmetry_check(input_str)

""" Python – Uppercase Half String """
# input_string='aditi'
# def findCentre(input_string):
#     return len(input_string)//2
# def upperHalfString(input_string,centre):
#     return input_string[:centre]+input_string[centre:].upper()
# result=upperHalfString(input_string,centre=findCentre(input_string))
# print(result)

""" Ways to remove i’th character from string in Python """
# # Method 1
# input_string='aditi_samarth'
# # remove 5th character
# output_string=" "
# for i in range(len(input_string)):
#     if i!=5:
#         output_string+=input_string[i]
# print(input_string,output_string)
