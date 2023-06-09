
n=input()
x=[]
for i in n:
    x.append([n.count('b'),n.count('a'),n.count('l')//2,n.count('o')//2,n.count('n')])
    break
for i in x:
    print(min(i))
