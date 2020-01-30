

def start(k,f):
    r,c=0,0
    r=int(k.split(',')[0])
    c=int(k.split(',')[1])
    try:
        if f==0 and game[r-1][c-1]=='':
            game[r-1][c-1]='x'
        elif f==1 and game[r-1][c-1]=='':
            game[r-1][c-1]='o'
        else:
            err(f,1)
            return
    except:
        err(f,0)
        return
    pri(game)
            
def err(f,q):
    if q==1:
        print('already given')
    else:
        print('out of range')
    if f==1:
        moves2()
    else:
        moves() 
def pri(game):
    for i in (game):
        print(i)
def moves():
    p1=input('enter player1 move(row,col) : ')
    start(p1,0)
def moves2():
    p2=input('enter player2 move(row,col) : ')
    start(p2,1)
    
def chance(game):
    c=0
    for i in range(len(game)):
        for j in range(len(game)):
            if game[i][j]=='':
                c+=1
    return c
                
        
if __name__=='__main__':
    print('\n here:\nplayer1 - x\tplayer2 - o')

    game=[['','',''],
          ['','',''],
          ['','','']]
    pri(game)
    while chance(game):
        moves()
        if chance(game):
            moves2()
 
    

    
  

    

