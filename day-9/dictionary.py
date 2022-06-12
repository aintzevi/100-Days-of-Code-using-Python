# Create dictionary of words and sentiment
terms = {
    "good": "positive",
    "bad": "negative",
    "great": "positive",
}


# print a specific entry/value
print(terms["great"])

# Add a new term in the dictionary
terms["awful"] = "negative"
print(terms)


# Create empty dictionary
empty_dictionary = {}
print(empty_dictionary)


# Edit a term in the dictionary
terms["awful"] = "strong negative"
print(terms)

# Loop through the dictionary and print the key-value pairs
for key in terms:
    print("Key: " + key + ", Value: " + terms[key])

# Wipe an existing dictionary
terms = {}
print(terms)
