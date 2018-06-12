import random 
secret = random.uniform(1,2)
new_sec = round(secret, 2)
print('-----let us play a game-----')
temp = input('来猜一猜现在我想的一个数字:')
guess = float(temp)
count = 1
while count <=3:
    if guess == new_sec:
        print('w0w')
        break
    if count == 3:
        print('没机会了')
        break
    if guess > new_sec:
        print('大了')
        temp = input('猜错了，请重新输入：')
        guess = float(temp)
        count += 1
    else:
        print('小了小了')
        temp = input('猜错了，请重新输入：')
        guess = float(temp)
        count += 1
print('game over')