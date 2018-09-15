a = input()
one = zero = 0
for i in range(len(a)):
    if a[i] == '1':
        one += 1
print(a,one%2,sep='')
