# take inputs
num = '-45721'

# calculate reverse of number
reverse = ''
for i in range(len(num), 0, -1):
   reverse += num[i-1]

# print reverse of number
print('The reverse number is =', reverse)
