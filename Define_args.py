# def sum(num1, num2, num3=5):
#     result = num1 + num2 + num3
#     return result
# total = sum(90,10)
# print('Total:',total )

#args
# def all_sum(*numbers): # "*" Can take more value
#     print(numbers)
#     sum = 0
#     for num in numbers:
#         print(num)
#         sum += num
#     return sum
# total = all_sum(1,2,3,4,5) #Unlimited value can assign
# print('Total:',total)
def do_a_lot(*args):
    print(args)
total = do_a_lot(1,2,3,4,5)