z = input()
a = input()
b = input()
for i in range(len(z)):
    doing = True
    for j in range(len(a)):
        if z[i]==a[j]:
            print(b[j],end='')
            doing=False
            break
        elif z[i]==b[j]:
            print(a[j],end='')
            doing=False
            break
    if doing:
        print(z[i],end='')
