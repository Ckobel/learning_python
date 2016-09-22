import sys
def sqrlength(n):
    sqrlen = -1
    for i in range(n):
        if len(str(i**2)) > sqrlen:
            sqrlen = len(str(i**2))
            print i, '^2 : ', i**2, '    len : ', sqrlen


sqrlength(int(sys.argv[1]))
