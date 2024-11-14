def filter_words(words, character):
    return [word for word in words if word and word[0].lower() == character]

words = ["Bosch", "bengaluru", "lenovo", "Rusin"]
character = 'b'
result = filter_words(words, character)

print(result)
