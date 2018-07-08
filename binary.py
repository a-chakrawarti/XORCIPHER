def dec2bin(n):
    a=n
    i=0
    b=n
    atemp=0
    byte=list()

    while i<7:
        a=int(a/2)
        b=b/2
        atemp=a
        if a==b:
            byte.append('0')
        else:
            byte.append('1')
        b=atemp
        i=i+1
    byte.reverse()
    byte=''.join(byte)
    return byte
