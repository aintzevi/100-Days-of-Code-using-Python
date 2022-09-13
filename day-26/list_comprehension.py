# Aka creating a list from a list directly

list = [1, 2, 3]

new_list = [x + 1 for x in list]
print(new_list)

name = "Katerina"

letters_list = [letter for letter in name]
print(letters_list)

double_nums = [num * 2 for num in range(1, 5)]
print(double_nums)

# Conditional List Comprehension

names = ["Anna", "Bob", "Caroline", "David", "Ellie", "Freddie"]
short_names = [name for name in names if len(name) <= 5]

print(short_names)

long_names_capitalized = [name.upper() for name in names if len(name) >= 5]
print(long_names_capitalized)
