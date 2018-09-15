mode = input()
z = input() ; Z = len(z)
a = input() ; A = len(a)
b = input()

def eiei(a,b):
    return ord(a) == ord(b) or ord(a)-32 == ord(b) or ord(a)+32 == ord(b)

def comp(i):
    I = i
    while i<Z and i-I<A:
        if not(eiei(z[i],a[i-I])):
          return False
        i+=1
    #print(I,i,i-I+1)
    return i-I == A

i=0
ST = ''
while i<Z:
    if eiei(z[i],a[0]) and comp(i) and mode!='':
        ST += b
        i  += A
        if mode=='R':
            mode=''
    else:
        ST += z[i]
        i += 1
print(ST)
