import numpy as np
import math
#输入
import sys
MAX=0


ops = [""]
def ismatch(str,lis):
    cc=-1
    for x in lis:
        cc=cc+1
        if str==x:
            return cc

    return 0

def main():
    OUT = np.zeros(100)
    xx=0



    while True:
        line = sys.stdin.readline()
        if not line:
            for z in ops:
                if z!= '':
                    print(z)
                    print('\n')
            break






        l = list(map(int, line.split()))
        M = l

        cc=0
        yy=0
        com=['']
        yuyin=['']
        maps=np.zeros(M[0]+1)
        for x in range(0, M[0]):
            line = input()
            l = list( line.split() )
            if ismatch(l[0],yuyin)==0:
                yuyin.append(l[0])
                cc=cc+1

            if ismatch(l[1],com) == 0:
                com.append(l[1])
                yy=yy+1
            maps[yy]=cc
        for x in range(0, M[0]):
            line = input()
            l = list(line.split())

            ops.append(  com[int(round(maps[ismatch(l[0],yuyin)]))]  )


















if "__main__"==__name__:
    main()