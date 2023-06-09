
#https://www.thecodemind.io/app/discription.php?pageCategory=c3pzTm1NaHFsYWVCeFpGMVpkTDloZz09&Tid=OHdVN2FDYlkvald1WWRWc2lwbW1kUT09&Pid=VXJoL1RIVUtlMW05Rm9md2FiSmRqdz09&Course=eUdCU2wyQVJUZGx4TjltZnFMNEtyZz09&Technology=L2RYTEdBRUMwdnh0Uzh5N0NlMU1iUT09&Topic=aDRlZkRZWHdrOXphL0VwNi9UVUdDZz09

n=input()
l=n.split(",")
s=''
for i in l:
    l1=[]
    l2=[]
    for j in i:
        if j.isdigit():
            l1.append(int(j))
        elif j.isalpha():
            l2.append(j)
    for i in range(len(l1)):
        s22=l1.index(max(l1))
        m=l1.pop(s22)
        if m<=len(l2):
            s+=l2[m-1]
            break
    else:
        s+="X"
print(s)
