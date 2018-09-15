a = input()
ch = [0]*10
for i in range(len(a)):
    ch[int(a[i])] += 1
No = True
for i in range(10):
    if ch[i]==0:
        print(i,end=" ")
        No = False
if No:
    print("No missing digits")
