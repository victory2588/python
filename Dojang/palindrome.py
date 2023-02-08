word=input('단어를 입력하세요: ')

is_pal=True
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        is_pal=False
        break

print(is_pal)

#더 쉬운 방법 2가지(슬라이스, reversed)#

'''word=input('단어를 입력하세요: ')
print(word==word[::-1])


word=input('단어를 입력하세요: ')
list(word)==list(reversed(word))
'''