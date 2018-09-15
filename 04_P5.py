def Sum(val,n):
    if n>=0:
        if '0'<=val[n] and val[n]<='9':
            return Sum(val,n-1) + int(val[n])
        return Sum(val,n-1)
    else:
        return 0
a,b = [stank for stank in input().split()]
a = a[0].upper() + a[1:].lower()
print(a,Sum(b,len(b)-1))
