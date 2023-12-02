s=0
for l in open('o'):
  u=l.split(" ")
  N={v[1]:int(v[0])for v in sorted(list(zip(u[2::2],[x[0]for x in u[3::2]])),key=lambda x:int(x[0]))}
  s+=(lambda a,b,c:a*b*c)(*N.values())
print s
