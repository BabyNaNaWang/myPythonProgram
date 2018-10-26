names = []
insertName = ''
insertSex = ''
insertPhone = ''
def printMenu():
    print('欢迎使用换名册')
    print('*'*30)
    print('1:添加信息')
    print('2:修改信息')
    print('3:删除信息')
    print('4:查询信息')
    print('5:显示所有信息')
    print('0:退出系统')
    print('*'*30)

def getStuInfo():
    global insertName
    global insertSex
    global insertPhone
    #3.1 提示用户输入一个新名字
    insertName = input('请输入一个新名字:')
    #3.2 提示用户输入性别
    insertSex = input('请输入性别：')
    #3.3 提示用户输入电话
    insertPhone = input('请输入电话号码：')
def addStuInfo():
    getStuInfo()
    stuInfos = {}
    stuInfos['name'] = insertName
    stuInfos['sex'] = insertSex
    stuInfos['phone'] = insertPhone
    names.append(stuInfos)
def editStuInfo():
    #修改学生信息
    # 提示并获取需要修改的学生序号
    stuId = int(input('请选择需要修改的学生序号：'))
    getStuInfo()
    names[stuId-1]['name'] = insertName
    names[stuId-1]['sex'] = insertSex
    names[stuId-1]['phone'] = insertPhone
def main():
    while True:
        # 1、提示操作
        printMenu()
        # 2、选择要操作的数字
        key = input('请选择您需要的操作：')

        # 3、根据选择做事情
        #定义列表
        if key == '1':
            addStuInfo()
        elif key == '2':
            editStuInfo()
        elif key == '3':
            #提示需要并获取需要删除的学生序号
            stuId = int(input('请选择需要修改的学生序号：'))
            del names[stuId-1]
        elif key == '4':
            #提示需要查看的学生序号
            stuId = int(input('请选择需要修改的学生序号：'))
            print('序号    姓名    性别    电话')
            print('%d     %s      %s      %s' % (stuId, names[stuId-1]['name'], names[stuId-1]['sex'], names[stuId-1]['phone']))
        elif key == '5':
            print('*'*30)
            print('学生信息如下')
            print('*'*30)
            print('序号      姓名      性别      手机号码')
            i = 1
            for tempInfo in names:
                print('%d        %s       %s        %s' %(i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
                i += 1
        elif key == '0':
            print('再来啊')
            break
main()
