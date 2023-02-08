a=list(map(int,input().split(";")))
for i in sorted(a,reverse=True):
    print('%9s'%format(i,','))


