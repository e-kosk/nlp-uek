import json
import re
from collections import Counter


def calculate_frequencies(text):
    text = ''.join(filter(str.isalpha, text))
    frequencies = Counter(text.lower())
    total = sum(frequencies.values())
    for letter in frequencies:
        frequencies[letter] = round(frequencies[letter] / total, 4)
    return frequencies


def compare_profiles(profile1, profile2):
    difference = 0
    for letter in set(profile1) | set(profile2):
        difference += abs(profile1.get(letter, 0) - profile2.get(letter, 0))
    return difference


def detect_language(text, model='model.json'):
    text_frequency = calculate_frequencies(text)
    best_match = None
    min_difference = float('inf')

    with open(model, 'r') as file:
        language_data = json.loads(file.read())

    for language, language_frequency in language_data.items():
        difference = compare_profiles(language_frequency, text_frequency)
        if difference < min_difference:
            min_difference = difference
            best_match = language

    return best_match


def split_into_sentences(text):
    no_break_line = ' '.join(text.split())
    return re.split(r'[\.\?] ', no_break_line)
    # return no_break_line.split('. ')


def profile_text(text):
    sentences = split_into_sentences(text)
    output = {}
    for sentence in sentences:
        lang = detect_language(sentence)
        output.setdefault(lang, 0)
        output[lang] += len(sentence)
    total = sum(output.values())
    result = {
        lang: lang_count / total
        for lang, lang_count in output.items()
    }
    return result


def train(base_dir, out='model.json'):
    output = {}

    for path in base_dir.iterdir():
        lang = path.stem
        with open(path, 'r') as file:
            frequencies = calculate_frequencies(file.read())
        output[lang] = frequencies

    with open(out, 'w') as file:
        file.write(json.dumps(output, indent=2))


def validate(base_dir, ):
    output = {}
    for path in base_dir.iterdir():
        lang = path.stem
        with open(path, 'r') as file:
            detected_language = detect_language(file.read())
        output[lang] = detected_language
    return output
