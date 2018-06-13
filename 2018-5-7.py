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
        temp = input('大了，请重新输入：')
        guess = float(temp)
        count += 1
    else:
        temp = input('小了，请重新输入：')
        guess = float(temp)
        count += 1
print('game over')