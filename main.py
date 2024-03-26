consonants = {'a': 'a', 'b': 'bob', 'c': 'coc', 'd': 'dod', 'e': 'e', 'f': 'fof',
              'g': 'gog', 'h': 'hoh', 'i': 'i', 'j': 'joj', 'k': 'kok',
              'l': 'lol', 'm': 'mom', 'n': 'non', 'o': 'o', 'p': 'pop',
              'q': 'qoq', 'r': 'ror', 's': 'sos', 't': 'tot', 'u': 'u',
              'v': 'vov', 'w': 'wow', 'x': 'xox', 'y': 'y', 'z': 'zoz'}

while True:
    text_conversion = input("Mata in text som ska översättas här: ").lower()
    converted_txt = ""

    for i in range(len(text_conversion)):
        key = text_conversion[i]
        if key in consonants:
            converted_txt += consonants[key] + ''
        else:
            converted_txt += key + ''
        
    print(converted_txt)
