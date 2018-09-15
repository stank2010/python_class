def re(a):
    stank = ''
    for i in range(len(a)):
        stank = a[i] + stank 
    return stank

lek = {'soon':0,'nueng':1 , 'song':2 , 'sam':3 , 'see':4 , 'ha':5 , 'hok':6 , 'jed':7 , 'pad':8 , 'kao':9 , 'ed':1 , 'yee':2 }
luk = {'sip':1 , 'roey':2 , 'pun':3 , 'muen':4 , 'saen':5 , 'larn':6}

Show = ''
adding = ''
Sum = 0
Arr = ['0']*12
jood = False
max_index = 0
temp_lek = -1

at = input()
mul = 0
#if at.find('larn'):
#    mul = 7

Heart = at.split('-')
for you in Heart:
    if you == 'lop':
        Show = '-'
        continue
    if you == 'jood':
        adding = '.'
        jood = True
        continue
    if jood:
        adding += str(lek[you])
    else:
        if you in lek:
            temp_lek = lek[you]
        elif you in luk:
            LEK = temp_lek
            if temp_lek == -1:
                LEK = 1

            
            if you == 'larn':
                for i in [9,8,7]:
                    if Arr[i-6]!='0':
                        Arr[i] = Arr[i-6]
                        max_index = max(i, max_index)
                    Arr[i-6] = '0'
                if temp_lek!=-1:
                    Arr[6] = str(temp_lek)
                    max_index = max(max_index,6)
                #mul = 7
            else:
                Arr[ mul + luk[you] ] = str(LEK)
                max_index = max(mul + luk[you] , max_index)
            
            #print(Arr)
            temp_lek = -1
if temp_lek!=-1:
    Arr[0] = str(temp_lek)

stank = ''
for i in range(max_index+1):
    stank += Arr[i]
    if (i+1)%3 == 0 and i != max_index:
        stank += ','

print(Show+re(stank)+adding)
