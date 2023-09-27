numbers = [5,7,9,15,20,25,30,40,45]
even=[]
# for num in numbers:
#     if num%2 == 0 and num%5 == 0:
#         even.append(num)
# print('even numbers are:',even)
# odd_num = [num for num in numbers if num%2 == 1 and num%5 == 0] #advance sign of for loop same as previous loop
# print(odd_num)
players = ['sakib', 'mushfiq', 'mustafiz']
ages = [35,36,28]
age_comb = []
for player in players:
    print('player:',player)
    for age in ages:
        # print(player, age)
        age_comb.append([player,age])
print(age_comb)

