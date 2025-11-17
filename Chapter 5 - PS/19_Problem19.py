'Count how many times each word appears in a sentence.'

def word_count(sentence):
    words = sentence.split()
    count_dict = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')  # Normalize the word
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict
sentence = "This is a test. This test is only a test."
result = word_count(sentence)
for word, count in result.items():
    print(f"'{word}': {count}")