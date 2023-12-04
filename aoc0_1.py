print(sum([int(b[0]+b[-1])for b in[[x for x in l if x.isdigit()]for l in open('o')]]))
