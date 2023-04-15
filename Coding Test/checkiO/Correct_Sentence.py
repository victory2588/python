def correct_sentence(text):
    text=text[0].upper()+text[1:]  # 첫 글자를 대문자로 바꾸고 두번째 글자부터 붙여줌

    if not text.endswith('.'):  # 끝이 무엇인지 알아낼 수 있음!
        text+='.'
    return text

print(correct_sentence("greetings, friends"))