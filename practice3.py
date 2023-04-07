from tensorflow.keras.preprocessing.text import Tokenizer

text = '나는 진짜 매우 매우 맜있는 밥을 엄청 마구 마구 마구 먹었다.'

token = Tokenizer()
token.fit_on_texts([text])

print(token.word_index) 
 #가장 많은놈이 앞으로 갔다.  {'마구': 1, '매우': 2, '나는': 3, '진짜': 4, '맜있는': 5, '밥을': 6, '엄청': 7, '먹었다': 8}
print(token.word_counts)
#OrderedDict([('나는', 1), ('진짜', 1), ('매우', 2), ('맜있는', 1), ('밥을', 1), ('엄청', 1), ('마구', 3), ('먹었다', 1)]) 단어횟수를 표시

x = token.texts_to_sequences([text])
print(x)