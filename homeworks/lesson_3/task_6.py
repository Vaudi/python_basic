"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

def int_func(word):

    word_list = list(word)
    word_list[0] = chr(ord(word_list[0]) - 32)
    return ''.join(word_list)


text = list((input('Введите текст: ').lower()).split())
text = ' '.join(list(map(int_func, text)))
print(text)