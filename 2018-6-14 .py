import random
select = random.randint(1,10)
print('让我们来玩一个游戏')
temp = input('输入一个数字猜大小')
guess = int(temp)
count = 0 
while count <= 2:
    if guess == select:
        print('我操')
        break
    if count == 2:
        print('么的机会了')
        break
    if guess > select:
        temp = input('大了')
        guess = int(temp)
        count += 1 
    else:
        temp = input('小了')
        guess = int(temp)
        count += 1
print('不玩了不玩了')
