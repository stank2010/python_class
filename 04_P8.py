def reverse(D,a,b):
    temp=""
    for i in range(a):
        temp+=D[i]
    i = a
    while i<=b:
        temp+=D[a+b-i]
        i+=1
    b+=1
    while b<len(D):
        temp+=D[b]
        b+=1
        
    return temp
D = input()
a,b = [int(stank) for stank in input().split()]
print(reverse(D,a,b))
