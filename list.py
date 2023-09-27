numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#index    -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(numbers[3],numbers[-3])

#start from the start but end before the end position
print(numbers[0:6]) 

#list(start:end:step)
print(numbers[1:7:1])
print(numbers[1:7:3])
print(numbers[4:]) #initial to 4  
print(numbers[:4])  #4 to last
print(numbers[:])  #all value
print(numbers[::-1]) #shortcut to reverse

