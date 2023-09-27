numbers = [4,3,2,1]
numbers.append(5)   #add at the last position
print(numbers) 
numbers.insert(4,9) #first one is the index and last one is the value
print(numbers)
# if 98 in numbers:
#     numbers.remove(98)
#     print(numbers)
# if 5 in numbers:
#     numbers.remove(5)   #it will remove the particular value
#     print(numbers)
last = numbers.pop() 
print(last, numbers)
if 3 in numbers:
    index = numbers.index(3)
    print('index number is:',index)
sorted = numbers.sort()
print('Sorted Number is:',numbers)
numbers.reverse()
print('reverse number:',numbers)



 

