s=0
for l in open('o'):
    l=l.split(": ")[1].split(" | ")
    k=len(set(l[0].split())&set(l[1].split()))
    s+=2**(k-1)if k else 0
print(s)
