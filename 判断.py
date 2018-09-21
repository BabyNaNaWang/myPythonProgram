money = 100
score = 0
for g in range(1,25):
    for m in range(1,17):
        for x in range(1,301):
            score == float(g)*2.5 +  float(m)*2/3  + float(x)/6
            if score == money and g+m+x==100 :
                print('鸡翁%s只，鸡婆%s只，鸡雏%s只'%(g,m,x))
            else:
                pass
    