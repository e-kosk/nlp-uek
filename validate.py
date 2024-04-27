from pathlib import Path

from core import validate

if __name__ == '__main__':
    BASE_DIR = Path('data/validation')
    results = validate(BASE_DIR)
    for lang, detected_lang in results.items():
        if lang == detected_lang:
            print(f'{lang}: SUCCESS')
        else:
            print(f'{lang}: FAIL ({detected_lang})')
