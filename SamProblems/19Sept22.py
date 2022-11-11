# # Find the number present odd number of times int []arr= {1,2,3,3,2}
# arr=[1,2,3,3,2,12,12,12,12,12]
# count_dict={}
# arrOddNumbers=[]
# for i in arr:
#     if i not in count_dict.keys():
#         count_dict[i]=arr.count(i)
# print(count_dict)
# for key,value in count_dict.items():
#     if value%2!=0:
#         arrOddNumbers.append(key)
# print(arrOddNumbers)

# # 2. *  Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the
# #  concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
# # Example 1:
# # Given words = ["bat", "tab", "cat"]
# # Return [[0, 1], [1, 0]]
# # The palindromes are ["battab", "tabbat"]
#
# words=['aaa','tab','cat','tac']
# listOfWords=[]
# for i in range(len(words)):
#     for j in range(len(words)):
#         concatWWord=words[i]+words[j]
#         concatWWordReverse=concatWWord[::-1]
#         if concatWWord==concatWWordReverse and i!=j:
#             listOfWords.append([i,j])
# print(listOfWords)

# 3.Given an array of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]]

input=['eat','tea','tan','ate','nat','bat']
firstInput1=input[0]
firstInput2=input[1]
firstInput3=input[2]
firstInput4=input[3]
firstInput5=input[4]
firstInput6=input[5]
# if sorted(list(firstInput1))==sorted(list(firstInput2)):
#     input.remove(firstInput2)
# if sorted(list(firstInput1))==sorted(list(firstInput3)):
#     input.remove(firstInput3)
# if sorted(list(firstInput1))==sorted(list(firstInput4)):
#     input.remove(firstInput4)
# if sorted(list(firstInput1))==sorted(list(firstInput5)):
#     input.remove(firstInput5)
# if sorted(list(firstInput1))==sorted(list(firstInput6)):
#     input.remove(firstInput6)
# print(input)
for i in range(0,len(input)-2):
    print(input[i])
    if sorted(list(input[0])) == sorted(list(input[i+1])):
        input.remove(input[i+1])
print(input)
output=[]
