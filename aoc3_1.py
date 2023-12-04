j=1
D={}
for l in open('o'):
  z=D.values()
  l=l.split(": ")[1].split(" | ")
  k=len({*l[0].split()}&{*l[1].split()})
  D[j]=list(range(j,k+j)),-~sum(v[1]for v in z if j-1 in v[0])
  j+=1
print(sum(v[1]for v in z))
