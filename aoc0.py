e=enumerate
S=['one','two','three','four','five',
    'six','seven','eight','nine']
k=0 
for l in open('o'):
    a=[(x,i)for i,x in e(l)if x.isdigit()]+[
    (`i+1`,l.find(x))for i,x in e(S)if x in l]+[
    (`i+1`,l.rfind(x))for i,x in e(S)if x in l]
    a.sort(key=lambda x:x[1])
    k+=int(a[0][0]+a[-1][0])
print(k)
