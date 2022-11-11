""" Check if two lists have at-least one element common """
# a=[1,2,3,4,5]
# b=[1,2,3,5,6]
# def common_data(a,b):
#     result=False
#     for i in a:
#         for j in b:
#             if i==j:
#                 result=True
#                 return  result
# print(common_data(a,b))

## Other Method
# def common_item(a,b):
#     set_a,set_b=set(a),set(b)
#     if (set_a & set_b):
#         return True
#     else:
#         return False
# print(common_item(a,b))

# # other method
# def common_item(a,b):
#     set_a,set_b=set(a),set(b)
#     if (set_a.intersection(set_b)):
#         return True
#     else:
#         return False
# print(common_item(a,b))

