def hor():
    print(' ---'*s)
def ver():
    print('|   '*(s+1))
if __name__=='__main__':
    s=int(input('enter size of the game board : '))
    for _ in range(s):
        hor()
        ver()
    hor()
