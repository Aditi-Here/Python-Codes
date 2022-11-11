# # Ques1: How do you reverse a string in Java?
# print("Python Program to Reverse a String")
# st = input("Enter Input String :")
# # print(st[::])
# new_st=[]
# # for i in range(len(st)):
# #     new_st.append(st[(len(st)-(i+1))])
# # print("Output Reverse string is :","".join(new_st))
#
# for i in range((len(st)-1),-1,-1):
#     new_st.append(st[i])
# print(new_st)

""" multiple approaches
st=""
s='aditi'
for i in s:
    st=i+st
print(st)


"""

# # Ques2: How do you determine if a string is a palindrome?
# # Palindrome means reverse of string is same as string itself.
# st = input("Enter Input String :")
# # print(st[::])
# new_st=[]
# for i in range(len(st)):
#     new_st.append(st[(len(st)-(i+1))])
# print("Output Reverse string is :",''.join(new_st))
#
# for i in range(len(st)):
#     if st[i]!=new_st[i]:
#         print("not palindrome string")
#         break
# else:
#     print('palindrome string')

# # Ques3: Find the number of occurrences of a character in a String.
# st = 'aditi'
# st_len=len(st)
# st_unique=set(st)
# count = 0
# # for x in st_unique:
# #     print(" The count of {} is {}".format(x,st.count(x)))
#
# for j in st_unique:
#     count=0
#     for x in range(st_len):
#         if j == st[x]:
#             count+=1
#     print("The count of {} is {}".format(j,count))

# # Ques4: How to find out if the given two strings are anagrams or not?
# st1="abcd"
# st2="acbd"
# ana_flag=True
# if len(st1)==len(st2):
#     for i in st1:
#         if (i not in st2) :
#             print("Its not anagrams string")
#             ana_flag=False
#
# if ana_flag:
#     print("Its an anagram string")


# # Ques5: How do you calculate the number of vowels and consonants in a String?
# vowels=['a','e','i','o','u']
# st='aditi'
# vovel_count=0
# st_len=len(st)
# for v in vowels:
#     for i in range(st_len):
#         if v in st[i]:
#             vovel_count+=1
# print("The vowel count is {} and consonent count is {}".format(vovel_count,st_len-vovel_count))

"""
here the problem is vowel list may be [A,E,I,O,U], case not considered
proper solution:
"""

# st="aditi"
# vowels=0
# consonent=0
# for x in st:
#     if (x=="a"or x=="A"or x=="e"or x=="E"or x=="i" or x=="I"
#             or x=="o" or x=="O" or x=="u" or x=="U"):
#         vowels+=1
#     else:
#         consonent+=1
# print("Vowels= {} and Consonent= {}".format(vowels,consonent))


