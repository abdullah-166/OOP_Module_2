#Local and Global variable using
balance = 3000
def buy_things(item,price):
    global balance   #We can use global variable by using this technique
    balance = balance - price
    # print('Balanace inside function:',balance)
    print(f'Balanace after buying {item}:',balance)

buy_things('Sunglass', 1000)