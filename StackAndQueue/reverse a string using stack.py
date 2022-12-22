stack=[]
str_input='aditi'
print('Input string is : ',str_input)
str_output=''
for i in range(len(str_input)):
    stack.append(str_input[i])
for i in range(len(stack)):
    str_output+=stack.pop()
print('Reverser string is: ',str_output)


