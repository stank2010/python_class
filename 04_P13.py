z = input()
a = input()
b = input()
for i in range(len(z)):
    if z[i]==a:
        print(b,end='')
    elif z[i]==b:
        print(a,end='')
    else:
        print(z[i],end='')
