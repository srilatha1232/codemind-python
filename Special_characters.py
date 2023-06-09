

n=input()
l1=[]
l2=[]
l3=[]
for i in n:
    if (i.isalpha()==False) and (i.isdigit()==False):
        l1.append(i)
    if i.isdigit():
        if int(i)%2==0:
            l2.append((i))
        else:
            l3.append((i))
s1=''
if len(l1)%2==0:
    if len(l2)<len(l3):
        for i in range(len(l2)):
            s1+=l2[i]
            s1+=l3[i]
        else:
            for j in range(len(l2),len(l3)):
                s1+=l3[j]
    else:
        for i in range(len(l3)):
            s1+=l2[i]
            s1+=l3[i]
        else:
            for j in range(len(l3),len(l2)):
                s1+=l2[j]
else:
    if len(l2)<len(l3):
        for i in range(len(l2)):
            s1+=l3[i]
            s1+=l2[i]
        else:
            for j in range(len(l2),len(l3)):

                s1+=l3[j]
    else:
        for i in range(len(l3)):
            s1+=l3[i]
            s1+=l2[i]
        else:
            for j in range(len(l3),len(l2)):
                s1+=l2[j]
print(s1)
