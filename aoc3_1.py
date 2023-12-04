j=1
D={}
for l in open('o'):
  z=D.values()
  l=l.replace("  ", " ").split(" | ")
  k=len({*l[0].split(": ")[1].split()}&{*l[1].split()})
  e=-~sum(v[1]for v in z if(j+1)in v[0])
  D[j+1]=[i+2 for i in range(j,k+j)],e
  j+=1
print(sum(v[1]for v in z))
