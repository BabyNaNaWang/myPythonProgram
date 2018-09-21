# 1代表车票通过，0代表车票不通过
chepiao = 0 

#管制器具长度判断

changdu = 9 

chepiaoFlag = 0
#判断是否有车票

if chepiao == 1:
    print('可以进入')
    chepiaoFlag = 1
else:
    print('请先去购买车票，然后再来按键')
if chepiaoFlag == 1 and changdu < 10:
    print('通过检票')
elif chepiaoFlag == 1 and changdu >= 10:
    print('按键不通过')
    