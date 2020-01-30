def check(l):
    for i in range(len(l)):
        if l[i]==3*['x']:
            print('player 1 win')
            return 0
        elif l[i]==3*['o']:
            print('player 2 win')
            return 0
    return 1
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
game=[['','','o'],
    ['','o',''],
    ['o','','']]
r=len(game)
print(win())
