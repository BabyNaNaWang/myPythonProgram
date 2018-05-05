import random 
secret = random.randint(1,10)
print('-----let us play a game-----')
temp = input('来猜一猜现在我想的一个数字:')
guess = int(temp)
while guess !=8:
    temp = input('猜错了，请重新输入：')
    guess = int(temp)
    if guess == 8:
        print('恭喜你答对了')
        print('没有奖励哦')
    else:
        if guess > 8:
            print('大了大了')
        else:
            print('小了小了')
print('game over')