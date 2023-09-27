# def full_name(first, last):
#     name = f'{first} {last}'
#     return name

# #name = full_name('Abdullah Al', 'Arif') serial wise parameter
# name = full_name(last='Arif',first='Abdullah Al', )
# print('Name:',name)

# def famous_name(first,last,title):
#     name = f'{title} {first} {last}'
#     return name
# name_ = famous_name(last='Hasan', first='Sabbir',title='Dr.')
# print(name_)

#define key **args
# def famous_name(first,last,**addition):
#     name = f'{first} {last}'
#     # print(addition['title'])
#     for key, value in addition.items():
#         print(key, value)
#     return name
# name_ = famous_name(last='Hasan', first='Sabbir',title='Md',addition='Dr.')
# print(name_)

#return multiple thing
def lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    sub = num1 - num2
    return sum,sub,mul
all = lot(9,8)
print('I do not know:',all)