from core import detect_language

if __name__ == '__main__':
    text = input('Type in some text: ')
    lang = detect_language(text)
    print(f'Detected language: {lang}')
