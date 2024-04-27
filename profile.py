from core import profile_text

if __name__ == '__main__':
    text = input('Type in some text: ')
    results = profile_text(text)
    for lang, value in results.items():
        print(f'{lang}: {value * 100:.0f}%')
