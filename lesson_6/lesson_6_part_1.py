
while True:
    text = input("Введите два слова:")
    word_count = len(text.split())
    word_count != 2
    text = input("Введите два слова:")

    first_word = text[:text.find(' ')]
    second_word = text[text.find(' ') + 1:]
    m = first_word[::-1]
    x = second_word[::-1]

    print(m.title(), x.title())
    break
