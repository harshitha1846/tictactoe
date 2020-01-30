li=[[1,2,3],
    [4,5,6],
    [7,8,9]]
for i in range(3):
    print(' ---'*3,end='')
    print()
    for j in range(3+1):
        if j==3:
           print('|',end='    ')
        else:
            print('|',end=' {} '.format(li[i][j]))
    print()
    if(i==3-1):
        print(' ---'*3,end='')
