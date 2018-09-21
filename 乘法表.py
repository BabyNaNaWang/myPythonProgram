i = 1 
while i<=9:
    hang = 1
    while hang <=i:
        print('%d*%d=%-2d '%(hang,i,hang*i),end='')
        hang += 1 
    print('')
    i+=1