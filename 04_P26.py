lek = ['soon','nueng','song','sam','see','ha','hok','jed','pad','kao','sip']
luk = ['','sip','roey','pun','muen','saen','larn']

def re(a):
  stank = ""
  i = len(a)-1
  while i>=0:
    stank += a[i]
    i-=1
  return stank

def COUNT(a):
    stank = ""
    i = 0
    A = len(a)
    while i<A:
        if i%6==0 and i>0:
          stank = 'larn-'+stank
        elif A==1 :
          stank = lek[ord(a[i])-48]
          break
        
        if i%6>0 and a[i]!='0':
          stank = luk[i%6] + '-' + stank
            
        if i+1<A and i%6 == 0 and a[i+1]>'0' and a[i]=='1':
            stank = 'ed-' + stank
        elif i%6 == 1 and a[i]=='2':
            stank = 'yee-' + stank
        elif not(a[i]=='1' and i%6==1) and a[i]!='0':
            stank = lek[ord(a[i])-48] + '-' + stank
            
        i+=1
        #print(stank,'/eeii')
    if stank[len(stank)-1]=='-':
      stank = stank[:len(stank)-1]
    return stank

a = input()
A_prime = ''
for i in a:
  if i!=',':
    A_prime += i
a = A_prime

if a[0]=='-':
  print('lop-',end='')
  a = a[1:]
if a.find('.') != -1:
    index = a.find('.')
    print(COUNT(re(a[:index])),'-jood',sep='',end='')
    for i in a[index+1:] :
      print('-',lek[ord(i)-48],sep='',end='')
else:
    print(COUNT(re(a)))
