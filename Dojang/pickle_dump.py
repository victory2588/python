import pickle

name='james'
age=17
address='서울시 종로구 혜화동'
scores={'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p','wb') as file:  # pickle.dump로 객체(값)를 저장할 때는 파일 모드를 'wb'로 지정해야함
    pickle.dump(name, file)         # b는 바이너리를 뜻함.
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)