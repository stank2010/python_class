z = input().lower()

Max = temp = int(len(z)>0)
for i in range(1,len(z)):
    if z[i] != z[i-1]:
        Max = max(Max,temp)
        temp = 1
    else:
        temp +=1
Max = max(Max,temp)
print(Max)
