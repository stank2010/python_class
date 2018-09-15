def check(sakan):
    n = len(sakan)
    for i in range(n//2):
        if sakan[i]!=sakan[n-i-1]:
            return "no"
    return "yes"

a = input()
temp = ""
a = a.lower()
for i in range(len(a)):
    if a[i]!=" ":
        temp += a[i]
print(check(temp))
