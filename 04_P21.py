def like(a,b,mode):
  stank = ""
  A = len(a)
  B = len(b)
  i = 0
  while (i<A and i<B and mode==1) or (A-i-1>=0 and B-i-1>=0 and mode==-1) :
    if mode==1:
      if a[i]!=b[i]:
        return stank
      stank = stank + a[i]
      
    if mode==-1:
      if a[A-i-1] != b[B-i-1]:
        return stank
      stank = a[A-i-1] + stank
    i+=1
  return stank

n = int(input())
pre = suf = input()
for i in range(n-1):
  b = input()
  pre = like(pre,b,1)
  suf = like(suf,b,-1)

if pre=='':
  print("NO COMMON PREFIX")
else:
  print(pre)

if suf=='':
  print("NO COMMON SUFFIX")
else:
  print(suf)
