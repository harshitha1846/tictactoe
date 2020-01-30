

def start(k,f,x):
    print(x)
    r,c=0,0
    r=int(k.split(',')[0])
    c=int(k.split(',')[1])
    if f==0 and game[r-1][c-1]=='':
            game[r-1][c-1]='x'
    elif f==1 and game[r-1][c-1]=='':
            game[r-1][c-1]='o'
    else:
        if f==0:
            x=-1
            #print(x)
            moves(x)
            
            return
        else:
            x=-1
            #print(x)
            moves2(x)
            return
    pri(game)
def pri(game):
    for i in (game):
        print(i)
def moves(n):
    p1=input('enter player1 move(row,col) : ')
    n+=1
    start(p1,0,n)
    if n<9:
        moves2(n)
def moves2(num):
    p2=input('enter player2 move(row,col) : ')
    num+=1
    start(p2,1,num)
    if num<9:
        moves(num)
if __name__=='__main__':
    print('\n here:\nplayer1 - x\tplayer2 - o')

    game=[['','',''],
          ['','',''],
          ['','','']]
    pri(game)
    num=0
    moves(num)
 
    

    
  

    

