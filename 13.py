def word_frequency(input_text):
    words = input_text.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_word_counts = dict(sorted(word_counts.items()))
    return sorted_word_counts

input_text = "some random sentance this is some random word"
result = word_frequency(input_text)

for word, count in result.items():
    print(f"{word}: {count}")
