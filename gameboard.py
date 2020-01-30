s=int(input('enter size of the game board : '))


for i in range(s):
    print(' ---'*s,end='')
    print()
    for _ in range(s+1):
        print('|',end='   ')
    print()
    if(i==s-1):
        print(' ---'*s,end='')
        

