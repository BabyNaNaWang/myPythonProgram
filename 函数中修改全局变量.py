#通过赋值语句直接修改全局变量
names = []
def test():
    names.append(11)
test()
print(names)