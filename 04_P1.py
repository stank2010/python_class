def change(IN,n):
    if n>=0:
        if IN[n]=='"' or IN[n]=="'" or IN[n]==',' or IN[n]=='.' or IN[n]=='(' or IN[n]==')':
            return change(IN,n-1)+" "
        return change(IN,n-1)+IN[n]
    else:
        return ""
a = input()
print(change(a,len(a)-1))
