# Keep the names in a list
with open("Input/Names/invited_names.txt", mode="r") as letter:
    list_of_names = letter.readlines()

# Iterate through the names list
for name in list_of_names:
    # Read the initial letter text
    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        # Write/Create new file for each name
        with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as invitation:
            # Replace the placeholder with the name and remove leading/following white spaces from the name
            invitation.write(starting_letter.read().replace("[name]", name.strip()))
