def starts_with_b(s):
    return s[0].lower() == 'b' if s else False

def ends_with_b(s):
    return s[-1].lower() == 'b' if s else False

def filter_strings(names, predicate):
    return [name for name in names if predicate(name)]

names = ["Bosch", "bengaluru", "lenovo", "BoB"]

# Filter names that start with 'b'
filtered_names_start = filter_strings(names, starts_with_b)
print(filtered_names_start)

# Filter names that end with 'b'
filtered_names_end = filter_strings(names, ends_with_b)
print(filtered_names_end)
