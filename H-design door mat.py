def design(row, col):
    for i in range(0,math.floor(row/2)):
        s='.|.'*i
        print(s.rjust(math.floor((col-2)/2),'-')+'.|.'+s.ljust(math.floor((col-2)/2),'-'))
    print('WELCOME'.center(col,'-'))
    for i in reversed(range(0,math.floor(row/2))):
        s='.|.'*i
        print(s.rjust(math.floor((col-2)/2),'-')+'.|.'+s.ljust(math.floor((col-2)/2),'-'))

import math
row, col=map(int, input().split())
design(row,col)