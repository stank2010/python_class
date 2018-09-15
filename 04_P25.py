a = input().strip()
multi = 1
Sum_sub = 0
Sum = 0

for i in range(len(a)):
    if a[i]=='+':
        Sum += Sum_sub*multi
        multi = 1
        Sum_sub = 0
    elif a[i]=='-':
        Sum += Sum_sub*multi
        multi = -1
        Sum_sub = 0
    else:
        Sum_sub = Sum_sub*10 + int(a[i])
    #print(Sum_sub)
Sum += Sum_sub*multi
print(Sum)
