import random
# 1、提示用户输入一个数字
while True:
    userInput = int(input('请选择 0、剪刀 1、石头 2、布：'))
    # 2、电脑随机生成一个数字
    sysNumber = random.randint(0,2)
    # 3、判断输赢并显示结果
    if (userInput == 0 and sysNumber == 2) or (userInput == 1 and sysNumber == 0) or (userInput == 2 and sysNumber == 1):
        print('winner winner chinken dinner')

    elif sysNumber == userInput:
        print('pingju')
    else:
        print('loser')