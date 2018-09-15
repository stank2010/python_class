def eyeei(a):
    ch = [0]*256
    for i in range(len(a)):
        if a[i]!=' ':
            ch[ord(a[i])]+=1
    return ch

def comp(a,b):
    for i in range(256):
        if a[i]!=b[i]:
            return False
    return True

a = input()
b = input()
if comp(eyeei(a.lower()),eyeei(b.lower())):
    print(a)
else:
    print(a,b)
