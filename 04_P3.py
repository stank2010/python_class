vowel = "aAeEiIoOuU"
sara = payun = 0
def Check(ai,a):
    for i in range(len(a)):
        if ai == a[i]:
            return True
    return False

a = input()
for i in range(len(a)):
    if ('a'<=a[i] and a[i]<='z') or ('A'<=a[i] and a[i]<='Z'):
        if Check(a[i],vowel):
            sara  += 1
        else:
            payun += 1
print(sara,payun)
