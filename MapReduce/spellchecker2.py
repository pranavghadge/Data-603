import langid
import re

def is_valid_word(word):
    return bool(re.match('^[a-zA-Z]+$', word))

def extract_non_english_words(line):
    non_english_words = []
    words = line.split()
    for word in words:
        if is_valid_word(word):
            lang, _ = langid.classify(word)
            if lang != 'en':
                non_english_words.append(word.lower())
    return non_english_words

def map_function(file_path):
    with open(file_path, 'r') as file:
        non_english_words = []
        for line in file:
            non_english_words += extract_non_english_words(line)
        return non_english_words

def reduce_function(words_list):
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Map phase
mapped_data = map_function('file2.txt')  # Use 'file1.txt' as the source file

# Reduce phase
reduced_data = reduce_function(mapped_data)

# Write the non-English words and their counts to a new file
with open('non_english_words.txt', 'w') as output_file:
    for word, count in reduced_data.items():
        output_file.write(f"{word}: {count}\n")
