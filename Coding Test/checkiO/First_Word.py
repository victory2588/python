def first_word(text):
    text=text.replace('.',' ').replace(',',' ').strip()  # replace를 사용하여 . , 를 공백으로 바꾸기
                                                         # strip 이용 앞뒤 공백 없애기
    text=text.split()  # 단어와 공백만 있는 경우 split를 사용하면 분리됨! 대박
    return text[0]

print(first_word("Hello world"))