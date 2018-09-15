def ch(ai):
    z = "aeiou"
    return z.find(ai)!=-1

a = input()
k = 0
found = False
for i in range(len(a)):
    if ch(a[i]):
        if found == False:
            found = True
            k+=1
    else:
        found = False
print(k)
