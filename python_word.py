def starts_with(name, char):
    return name[0].lower() == char.lower()

def ends_with(name, char):
    return name[-1].lower() == char.lower()

def filter_strings(names, predicate, char=None):
    if char:
        return [name for name in names if predicate(name, char)]
    return [name for name in names if predicate(name)]

names = ["Bosch", "bengaluru", "lenovo", "Bob"]
letter = 'b'
filtered_names_start = filter_strings(names, starts_with, letter)
filtered_names_end = filter_strings(names, ends_with, letter)

print(f"Filtered names starting with {letter}:", filtered_names_start)
print(f"Filtered names ending with {letter}:", filtered_names_end)
