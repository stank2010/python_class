z = input()
ch = [0]*256
for i in range(len(z)):
    ch[ord(z[i])]+=1

real = [0]*256
for i in range(len(z)):
    real[ord(z[i])]+=1
    if real[ord(z[i])]==2 or ch[ord(z[i])]==1:
        print(z[i],end='')
