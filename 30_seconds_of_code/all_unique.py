def all_unique(a):
    return len(a)==len(set(a))

x=[1,2,3,4]
y=[1,1,3,4]
print(all_unique(x))
print(all_unique(y))
