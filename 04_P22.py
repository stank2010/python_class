lek = ['zero','one','two','three','four','five','six','seven','eight','nine']
def ch(a):
    if '0'<=a and a<='9':
        return ord(a)-48
    return -1
def ch2(a):
    return ('a'<=a<='z') or ('A'<=a<='Z')

z = input()
if ch(z[0])==-1:
    print(z[0],end='')
else:
    print(ch(z[0]),end='')
    
for i in range(1,len(z)):
    A = ch(z[i])
    
    if ch(z[i-1])!=-1 and ( ch2(z[i]) or ch(z[i])!=-1 ):
            print(" ",end='')
            
    if  A != -1:
        print(lek[A],end='')
    else:
        print(z[i],end='')
