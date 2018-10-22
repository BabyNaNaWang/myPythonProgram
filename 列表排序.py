import random
#列表排序
nums = [1,34,5,90,80]
'''nums.sort(reverse = True)
print(nums)'''
nums.reverse()
print(nums)


newNums = [100,20,18,39,90]
#newNums.reverse() #倒置
#newNums.sort() #从小到大排序
newNums.sort(reverse = True) #从大到小排序
print(newNums)

#列表的常见操作
#1、添加 insert
names = ['he','she','his']
names.insert(0,'him')
print(names)
#2、添加append
names1 = ['he', 'she', 'his']
names.append('hah')
print(names1)
# 3、extend 
names1.extend(names)
print(names1)
print(names)

ss = random.sample(range(1,35),6)
ss.sort()
print(ss)
ss.sort(reverse = True)
print(ss)
ss.reverse()
print(ss)

xiaBiao = 'hello'
print(xiaBiao[::-1])

a = 10
b = 20
a,b = b,a 
print(a)
print(b)