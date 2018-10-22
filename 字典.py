'''myInfo = {'name':'wang','sex':'f','wife':'eeee'}
print(myInfo['name'])
print(myInfo.get('sex1','bu知道'))
myInfo['name'] = 'li'
print(myInfo)
myInfo['age'] = 18
print(myInfo)'''
myInfo = {'name': 'wang', 'sex': 'f', 'wife': 'eeee'}
del myInfo['wife']
print(myInfo)
myInfo = {'name': 'wang', 'sex': 'f', 'wife': 'eeee'}
myInfo.clear()
print(myInfo)