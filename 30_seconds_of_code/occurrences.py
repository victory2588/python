def count_occurrences(a,val):
    return len([x for x in a if x== val and type(x)==type(val)])  # 이게 뭐지?

print(count_occurrences([1,1,2,3,4,1],1))




