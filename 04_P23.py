def comp(a):
  return a=='"' or a=="'" or a=="," or a=='.' or a==" "

a = " " + input().lower() + " "
b = input().lower()
a_len = len(a)
b_len = len(b)

not_do = True
for i in range(a_len):
  if comp(a[i]):
    I = 1
    Jayrun = ""
    while I <= b_len and i+I < a_len:
      Jayrun += a[i+I]
      I+=1
      
    if Jayrun == b and comp(a[ i + b_len +1 ]):
        print("Found")
        not_do = False
        break
  
if not_do:
  print("Not Found")
