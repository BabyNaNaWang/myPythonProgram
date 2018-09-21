import random
a = random.randint(1,10)
print('随机到的整数为%s'%a)

b = random.random()
print('随机到的小数为%s' %b)

c = random.uniform(1.1,5.1)
print('随机到的小数为%s' %c)

d = random.choice('kevin')
print('抽泣到的内容为%s' %d)

e = random.randrange(1,100,2)
print('随机到的为%s' %e)

f = [1,2,3,4,5,6,7]
random.shuffle(f)
print(f)

g = random.sample('dafdgdfd',3)
print(g)