from typing import List, Callable
Predicate = Callable[[str], bool]
def starts_with_char(character: str) -> Predicate:
    return lambda word: word and word[0].lower() == character.lower()

def filter_words(words: List[str], predicate: Predicate) -> List[str]:
    return list(filter(predicate, words))

words = ["Bosch", "bengaluru", "lenovo", "Rusin"]
character = 'b'

predicate = starts_with_char(character)

result = filter_words(words, predicate)

print(result)
