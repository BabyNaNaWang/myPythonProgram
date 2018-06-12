import random 
secret = random.randint(1,10)
print(secret)
print('-----let us play a game-----')
temp = input('来猜一猜现在我想的一个数字:')
guess = int(temp)
i = 1
while i:
    if guess == secret:
        print('w0w')
        break
    if i == 3:
        print('没机会了')
        break
    while i < 3:
        i += 1
        if guess > secret:
            print('大了')
            temp = input('猜错了，请重新输入：')
            guess = int(temp)
        else:
            print('小了小了')
            temp = input('猜错了，请重新输入：')
            guess = int(temp)
print('game over')