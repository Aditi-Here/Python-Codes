# Method 1
# myDict={'a':12,'b':46,'d':46}
# if 'c' in myDict:
#     print(myDict['c'])
# else:
#     print("Key not found")

country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# search dictionary for country code of India
print(country_code.get('India', 'Not Found'))

# search dictionary for country code of Japan
print(country_code.get('Japan', 'Not Found'))

print(country_code)

country_code.setdefault('Japan',"Not found")
print(country_code)