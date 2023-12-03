import re
n=''
t=p=0
s=re.sub(r"[*@#/&=%+$-]",'!',open('o').read())
p=len(s.split('\n'))+1
for i,c in enumerate(s):
    if c.isdigit():n+=c
    elif n:
        if'!'in s[i+~len(n)]+c+s[i+~len(n)+p:i+p+1]+s[i-len(n)+~p:i-p+1]:t+=int(n)
        n=''
print t
