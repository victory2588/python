import string
a=input().split()
count=0
for i in a:
    if i.strip(string.punctuation)=='the':
        count+=1
print(count)