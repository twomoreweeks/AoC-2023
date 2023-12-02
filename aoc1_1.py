# one-liner 
print sum(min({int(k)<dict(r=13,g=14,b=15)[u[3::2][j][0]]for(j,k)in enumerate(u[2::2])})*int(u[1][:-1])for l in open('f')for u in[l.split(' ')])

# or a simpler alternative
s=0
for l in open('f'):
  u=l.split(" ")
  s+=min({int(k)<dict(r=13,g=14,b=15)[u[3::2][j][0]]for(j,k)in enumerate(u[2::2])})*int(u[1][:-1])
print s
