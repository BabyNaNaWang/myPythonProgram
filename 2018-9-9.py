'''numb1 = input('请输入第一个数字：')
numb2 = input('请输入第二个数字：')
result = int(numb1) + int(numb2)
print('%s + %s = %s'%(numb1,numb2,result)'''
'''age = input('请输入年龄：') 
age = int(age)
if age > 18:
    print('可以上网')
else:
    print('年龄太小')'''

intergral = int(input('请输入驾驶证当前积分：'))
role = int(input('请输入您违反的规则 1、闯红灯；2、违章停车：'))
if role == 1:
    intergral -= 6
if role == 2:
    intergral -= 3
print('您当前的分数为%d'%intergral)
if intergral <= 0:
    print('需要参加学习')
else:
    print('您当前的分数还剩%s,不需要学习'%intergral)