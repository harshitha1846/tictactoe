from random import *
li=[[2,2,1],
    [2,2,0],
    [2,1,1]]
r=len(li)
def check(l):
    for i in range(len(l)):
        if l[i]==r*[1]:
            print('player 1 win')
        elif l[i]==r*[2]:
            print('player 2 win')
        else:
            pass
def trans():
    res1,res2=[],[]
    j=r-1
    for i in range(r):
        res1.append(li[i][i])
        if j>=0:
            res2.append(li[i][j])
            j-=1
    check([res1])
    check([res2])
def col():
    li2=[]
    for i in range(r):
        t=[]
        for j in range(r):
            t.append(li[j][i])
        li2.append(t)
    #print(li2)
    check(li2)
    
            
        
if __name__=='__main__':
    check(li)
    trans()
    col()
    
    
    

    
    


