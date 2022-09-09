PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for name in invited_names:
        new_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, new_name)
        with open(f"Output/ReadyToSend/letter_for_{new_name}.docx", mode="w") as finished_letter:
            finished_letter.write(new_letter)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
