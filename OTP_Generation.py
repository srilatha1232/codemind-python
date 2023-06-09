s=input()
s1=''
for i in s:
    if int(i)%2:
        s2=(int(i)**2)
        s1=s1+str(s2)
print(s1)
