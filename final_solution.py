#it splits input and update value in game list
#here f=1 means user2 and f=1 means user1
def start(k,f):
    r,c=0,0
    try:
        r=int(k.split(',')[0])
        c=int(k.split(',')[1])
    
        if f==0 and game[r-1][c-1]==' ':
            game[r-1][c-1]='x'
        elif f==1 and game[r-1][c-1]==' ':
            game[r-1][c-1]='o'
        else:
            err(f,1)
            return
    except:
        err(f,0)
        return
    pri(game)
#if any error occurs during user input
def err(f,q):
    if q==1:
        print('already given')
    else:
        print('out of range')
    if f==1:
        moves2()
    else:
        moves()
#to display game
def pri(game):
    for i in range(3):
        print(' ---'*3,end='')
        print()
        for j in range(3+1):
            if j==3:
               print('|',end='    ')
            else:
                print('|',end=' {} '.format(game[i][j]))
        print()
        if(i==3-1):
            print(' ---'*3,end='')
    print()
#user1 input       
def moves():
    p1=input('enter player1 move(row,col) : ')
    start(p1,0)
#user2 input
def moves2():
    p2=input('enter player2 move(row,col) : ')
    start(p2,1)
#to check all squares are full or not
def chance(game):
    c=0
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j]==' ':
                c+=1
    return c
#to check any player wins or not
def check(l):
    for i in range(len(l)):
        if l[i]==3*['x']:
            print('player 1 win')
            return 0
        elif l[i]==3*['o']:
            print('player 2 win')
            return 0
    return 1
# if any player win it stops function
def win():
    a=check(game)
    if a==1:
        b=trans()
        if b==1:
            c=col()
            return c
        else:
            return 0
    else:
        return 0
#to find diagonal of game inorder to check players win 
def trans():
    res1,res2=[],[]
    j=r-1
    for i in range(r):
        res1.append(game[i][i])
        if j>=0:
            res2.append(game[i][j])
            j-=1
    a=check([res1])
    if a==1:
        b=check([res2])
        return b
    else:
        return 0
#to find col of game inorder to check players win     
def col():
    li2=[]
    for i in range(r):
        t=[]
        for j in range(r):
            t.append(game[j][i])
        li2.append(t)
    #print(li2)
    a=check(li2)
    return a
#main     
if __name__=='__main__':
    print('\n***********************************tictactoe GAME*************************************************\n')
    print('\n here:\nplayer1 - x\tplayer2 - o')

    game=[[' ',' ',' '],
          [' ',' ',' '],
          [' ',' ',' ']]
    r=len(game)
    pri(game)
    if input('start the game y|n : ')=='y':
        while chance(game) and win():
            moves()
            if chance(game) and win():
                moves2()
            else:
                break
    else:
        print('thank u')
 
    

    
  

    

